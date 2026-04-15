"""
simulate_feedback_interactive.py
---------------------------------
Simulasi interaktif HITL (Human-in-the-Loop) untuk skripsi IL EcoBin.

Alur:
1. Baca gambar satu per satu dari test set (acak)
2. Backbone mengekstrak fitur → Classifier memprediksi kelas + confidence
3. Jika confidence < TAU → trigger feedback: tanya user apakah prediksi benar
4. Jika user memberi koreksi → simpan ke feedback buffer
5. Setelah N_FEEDBACK sampel terkumpul → jalankan satu incremental cycle
6. Update prototype + retrain classifier head
7. Simpan model terbaru

Cara Pakai (di Jupyter):
    from simulate_feedback_interactive import run_interactive_session
    run_interactive_session(backbone, classifier, prototypes, test_dataset, device)
"""

import random
import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader, Subset
import torchvision.transforms as T
from torchvision import datasets
from PIL import Image
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt

# ─── Konstanta ─────────────────────────────────────────────────────────────────
CLASS_NAMES   = ['organic', 'recycle', 'residue', 'reusable']
TAU           = 0.75       # Threshold confidence untuk trigger feedback
N_FEEDBACK    = 10         # Jumlah feedback yang dikumpulkan sebelum update
N_EPOCHS_FT   = 5         # Epoch fine-tuning classifier head per cycle
ETA           = 0.1        # Prototype enhancement rate
H_BANDWIDTH   = 0.5        # KDE bandwidth
FEATURE_DIM   = 1280       # Dimensi fitur MobileNetV3

val_transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


# ─── Helper: Predict satu gambar ───────────────────────────────────────────────
def predict_image(backbone, classifier, image_tensor, device):
    """Prediksi satu gambar. Return: (class_name, confidence)"""
    backbone.eval(); classifier.eval()
    with torch.no_grad():
        feat   = backbone(image_tensor.unsqueeze(0).to(device))
        probs  = torch.softmax(classifier(feat), dim=1)[0]
        conf, pred_idx = probs.max(0)
    return CLASS_NAMES[pred_idx.item()], conf.item()


# ─── Helper: Prototype Enhancement ─────────────────────────────────────────────
def prototype_enhancement(prototype, new_features, eta=ETA):
    mu, H = prototype['mu'], prototype['H']
    H_inv = torch.linalg.pinv(H)
    enhanced = []
    for x in new_features:
        diff   = x - mu
        d_val  = torch.sqrt(diff @ H_inv @ diff).item()
        e_unit = diff / (diff.norm() + 1e-8)
        enhanced.append(mu + eta * d_val * e_unit)
    return torch.stack(enhanced) if enhanced else new_features


def compute_prototype(features, h=H_BANDWIDTH):
    N, mu = len(features), features.mean(0)
    XtX   = features.T @ features
    H     = h * (N - 1) * torch.linalg.pinv(XtX)
    return mu, H, N


def update_prototype(old_proto, new_feats, h=H_BANDWIDTH):
    combined = torch.cat([old_proto['features'], new_feats], 0)
    mu, H, N = compute_prototype(combined, h)
    return {'mu': mu, 'H': H, 'N': N, 'features': combined}


# ─── Helper: Evaluasi akurasi cepat ────────────────────────────────────────────
def quick_eval(backbone, classifier, dataloader, device):
    backbone.eval(); classifier.eval()
    correct = total = 0
    with torch.no_grad():
        for imgs, lbls in dataloader:
            preds = classifier(backbone(imgs.to(device))).argmax(1).cpu()
            correct += (preds == lbls).sum().item()
            total   += lbls.size(0)
    return correct / total if total > 0 else 0.0


# ─── Helper: Incremental Update dari feedback ──────────────────────────────────
def incremental_update_from_feedback(backbone, classifier, prototypes, feedback_buffer, device):
    """
    Lakukan satu incremental cycle dari feedback buffer.
    feedback_buffer: dict {class_name: [img_tensor, ...]}
    """
    ce_loss_fn = nn.CrossEntropyLoss()
    optimizer  = optim.Adam(classifier.parameters(), lr=5e-4)

    print("\n🔄 Memulai incremental update dari feedback...")
    train_x, train_y = [], []

    for cls_idx, cls in enumerate(CLASS_NAMES):
        if cls not in feedback_buffer or len(feedback_buffer[cls]) == 0:
            print(f"   [{cls}] Tidak ada feedback baru. Skip.")
            continue

        imgs = torch.stack(feedback_buffer[cls])

        # Ekstrak fitur
        backbone.eval()
        with torch.no_grad():
            feats = backbone(imgs.to(device)).cpu()

        # Prototype Enhancement
        enhanced = prototype_enhancement(prototypes[cls], feats)

        # Update prototype
        prototypes[cls] = update_prototype(prototypes[cls], feats)

        train_x.append(feats)
        train_x.append(enhanced)
        train_y.append(torch.full((len(feats),), cls_idx))
        train_y.append(torch.full((len(enhanced),), cls_idx))
        print(f"   [{cls}] {len(feats)} sampel dipakai + {len(enhanced)} enhanced.")

    if not train_x:
        print("   ⚠️ Tidak ada sample untuk update. Kembali.")
        return classifier, prototypes

    X, Y = torch.cat(train_x).to(device), torch.cat(train_y).to(device)

    classifier.train()
    for ep in range(N_EPOCHS_FT):
        optimizer.zero_grad()
        loss = ce_loss_fn(classifier(X), Y)
        loss.backward()
        optimizer.step()
        print(f"   Epoch {ep+1}/{N_EPOCHS_FT} — Loss: {loss.item():.4f}")

    print("✅ Incremental update selesai.")
    return classifier, prototypes


# ─── Fungsi Utama: Sesi Interaktif ─────────────────────────────────────────────
def run_interactive_session(backbone, classifier, prototypes, test_dataset, device,
                             valid_loader=None, n_samples=30,
                             tau=TAU, n_feedback=N_FEEDBACK):
    """
    Jalankan sesi simulasi interaktif.

    Args:
        backbone        : MobileNetV3 backbone (frozen)
        classifier      : Final linear classifier
        prototypes      : Dict prototype per kelas {cls: {'mu': ..., 'H': ..., ...}}
        test_dataset    : torchvision ImageFolder
        device          : torch.device
        valid_loader    : DataLoader untuk evaluasi (opsional)
        n_samples       : Jumlah gambar yang akan ditampilkan
        tau             : Threshold confidence (0.0 - 1.0)
        n_feedback      : Jumlah feedback sebelum trigger update
    """
    random.seed(None)  # Randomize seed untuk variasi simulasi
    all_indices = list(range(len(test_dataset)))
    selected    = random.sample(all_indices, min(n_samples, len(all_indices)))

    feedback_buffer   = defaultdict(list)
    total_feedback    = 0
    cycle_count       = 0
    session_stats     = {'shown': 0, 'feedback': 0, 'updates': 0, 'auto_accepted': 0}

    print("=" * 60)
    print("  🤖 SIMULASI HITL — ECOBIN INCREMENTAL LEARNING")
    print("=" * 60)
    print(f"  Total gambar: {n_samples} | Threshold τ={tau} | Feedback/update: {n_feedback}")
    print("  Ketik label baru jika mau koreksi. Tekan Enter jika benar.")
    print("  Ketik 'q' kapan saja untuk berhenti.\n")

    for i, idx in enumerate(selected):
        img_tensor, true_label_idx = test_dataset[idx]
        true_label  = test_dataset.classes[true_label_idx]
        pred_label, confidence = predict_image(backbone, classifier, img_tensor, device)

        session_stats['shown'] += 1

        print(f"\n[{i+1}/{n_samples}] Gambar #{idx}")
        print(f"  Prediksi : {pred_label.upper():<10} | Confidence: {confidence:.2%}")
        print(f"  Label Asli (simulasi): {true_label}")  # Hanya untuk simulasi

        # Tampilkan gambar jika posibble
        try:
            img_path = test_dataset.samples[idx][0]
            img      = Image.open(img_path)
            plt.figure(figsize=(3, 3))
            plt.imshow(img)
            plt.title(f"Prediksi: {pred_label} ({confidence:.0%})")
            plt.axis('off')
            plt.tight_layout()
            plt.show()
        except Exception:
            pass  # Gambar tidak tampil, tetap lanjut

        # Cek apakah perlu trigger feedback
        if confidence >= tau:
            print(f"  ✅ Confidence tinggi ({confidence:.0%}) → Diterima otomatis.")
            session_stats['auto_accepted'] += 1
            continue

        # Confidence rendah → tanya user
        print(f"\n  ⚠️ Confidence RENDAH ({confidence:.0%}) — Mohon verifikasi.")
        print(f"  Pilihan kelas: {', '.join(CLASS_NAMES)}")
        user_input = input(f"  Koreksi label? (Enter=benar, atau tulis kelas baru, 'q'=keluar): ").strip().lower()

        if user_input == 'q':
            print("\n⛔ Sesi dihentikan oleh user.")
            break
        elif user_input == '':
            print(f"  👍 User konfirmasi prediksi benar: {pred_label}")
            feedback_buffer[pred_label].append(img_tensor)
            total_feedback += 1
            session_stats['feedback'] += 1
        elif user_input in CLASS_NAMES:
            print(f"  ✏️  User koreksi: {pred_label} → {user_input}")
            feedback_buffer[user_input].append(img_tensor)
            total_feedback += 1
            session_stats['feedback'] += 1
        else:
            print(f"  ❌ '{user_input}' bukan kelas yang valid. Dilewati.")
            continue

        # Cek apakah sudah cukup feedback untuk trigger update
        if total_feedback >= n_feedback:
            cycle_count += 1
            print(f"\n📦 Feedback buffer penuh ({total_feedback} sampel) → Cycle #{cycle_count}")
            classifier, prototypes = incremental_update_from_feedback(
                backbone, classifier, prototypes, feedback_buffer, device)
            session_stats['updates'] += 1

            # Evaluasi setelah update
            if valid_loader is not None:
                acc = quick_eval(backbone, classifier, valid_loader, device)
                print(f"📊 Akurasi setelah Cycle #{cycle_count}: {acc:.4f}")

            # Reset buffer
            feedback_buffer.clear()
            total_feedback = 0

    # ─── Ringkasan Sesi ────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  📋 RINGKASAN SESI SIMULASI")
    print("=" * 60)
    print(f"  Gambar ditampilkan    : {session_stats['shown']}")
    print(f"  Diterima otomatis     : {session_stats['auto_accepted']}")
    print(f"  Feedback dikumpulkan  : {session_stats['feedback']}")
    print(f"  Cycle update dilakukan: {session_stats['updates']}")

    if valid_loader:
        final_acc = quick_eval(backbone, classifier, valid_loader, device)
        print(f"  Akurasi akhir sesi    : {final_acc:.4f}")

    print("=" * 60)

    return classifier, prototypes
