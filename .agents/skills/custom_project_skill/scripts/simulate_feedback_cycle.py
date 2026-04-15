"""
simulate_feedback_cycle.py — Simulasi T incremental cycle dari human feedback

Script ini mensimulasikan proses incremental learning:
1. Bagi dataset_incremental_simulation/ menjadi T cycle dengan N sample per cycle
2. Jalankan update prototype per cycle (Han et al. 2024 method)
3. Evaluasi setelah setiap cycle dan tracking forgetting metrics

Kolaborasi dengan:
- compute_baseline_prototypes.py → baseline_prototypes.pt
- evaluate_forgetting.py → ForgettingTracker

Usage:
    python scripts/simulate_feedback_cycle.py \
        --checkpoint mobilenetv3_MX150_best.pth \
        --prototypes baseline_prototypes.pt \
        --feedback_data dataset_incremental_simulation \
        --eval_data dataset_kating_cropped/test \
        --T 5 --N 30 \
        --eta 0.1 --h 0.5 --gamma 0.5 --lam 0.1
"""

import argparse
import json
import random
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Subset
from torchvision.datasets import ImageFolder


CLASSES = ['organic', 'recycle', 'residue', 'reusable']

# ─── Model Utilities ─────────────────────────────────────────────────────────

def load_model(checkpoint_path: str) -> Tuple[nn.Module, nn.Module]:
    """Kembalikan (feature_extractor, full_model)."""
    model = models.mobilenet_v3_large(weights=None)
    model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, len(CLASSES))

    checkpoint = torch.load(checkpoint_path, map_location='cpu')
    state_dict = checkpoint.get('model_state_dict', checkpoint.get('state_dict', checkpoint))
    model.load_state_dict(state_dict)

    # Feature extractor = semua kecuali classifier head
    feature_extractor = nn.Sequential(*list(model.children())[:-1])
    for p in feature_extractor.parameters():
        p.requires_grad_(False)  # Freeze backbone (Liu et al. 2023)

    return feature_extractor, model


# ─── Prototype Update (Han et al. 2024) ─────────────────────────────────────

def update_prototype(
    prototypes: Dict,
    class_name: str,
    new_features: torch.Tensor,
    eta: float,
    h: float,
) -> Dict:
    """
    Update prototype untuk satu kelas dengan new_features dari feedback.
    
    Implementasi Han et al. 2024:
    1. Hitung mean vector baru (Eq. 1)
    2. Hitung bandwidth matrix H baru (Eq. 7)
    3. Generate enhanced prototypes (Eq. 2)
    """
    old_proto = prototypes.get(class_name)
    N_new = new_features.shape[0]

    if old_proto is None:
        # Kelas baru dalam prototype (tidak terjadi di proyek ini — 4 kelas tetap)
        mu = new_features.mean(dim=0)
        XtX = new_features.T @ new_features
        H = h * (N_new - 1) * torch.linalg.pinv(XtX)
        prototypes[class_name] = {'mu': mu, 'H': H, 'N': N_new}
        return prototypes

    # Gabungkan fitur lama (diwakili oleh mu) dengan fitur baru
    N_old = old_proto['N']
    mu_old = old_proto['mu']

    # Update mean vector (weighted average)
    mu_new = (N_old * mu_old + new_features.sum(dim=0)) / (N_old + N_new)

    # Update bandwidth matrix dengan combined data
    # Approximate: gunakan hanya new_features untuk recompute H
    XtX = new_features.T @ new_features
    try:
        H_new = h * (N_new - 1) * torch.linalg.inv(XtX)
    except Exception:
        H_new = h * (N_new - 1) * torch.linalg.pinv(XtX)

    prototypes[class_name] = {
        'mu': mu_new,
        'H': H_new,
        'N': N_old + N_new,
    }
    return prototypes


# ─── Evaluation ──────────────────────────────────────────────────────────────

@torch.no_grad()
def evaluate(model: nn.Module, dataloader: DataLoader, device: str) -> Dict[str, float]:
    """Hitung per-class accuracy."""
    model.eval()
    idx_to_class = {v: k for k, v in dataloader.dataset.class_to_idx.items()}
    correct = defaultdict(int)
    total = defaultdict(int)

    for images, labels in dataloader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        preds = outputs.argmax(dim=1)

        for pred, label in zip(preds, labels):
            cls = idx_to_class[label.item()]
            total[cls] += 1
            if pred == label:
                correct[cls] += 1

    return {cls: correct[cls] / max(total[cls], 1) for cls in CLASSES}


# ─── Main Simulation ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Simulasi Incremental Learning Cycle — IL EcoBin")
    parser.add_argument('--checkpoint', default='mobilenetv3_MX150_best.pth')
    parser.add_argument('--prototypes', default='baseline_prototypes.pt')
    parser.add_argument('--feedback_data', default='dataset_incremental_simulation')
    parser.add_argument('--eval_data', default='dataset_kating_cropped/test')
    parser.add_argument('--T', type=int, default=5, help='Jumlah incremental cycle')
    parser.add_argument('--N', type=int, default=30, help='Sample per cycle')
    parser.add_argument('--eta', type=float, default=0.1, help='Uncertainty scale η')
    parser.add_argument('--h', type=float, default=0.5, help='KDE bandwidth h')
    parser.add_argument('--gamma', type=float, default=0.5, help='Prototype loss weight γ')
    parser.add_argument('--lam', type=float, default=0.1, help='Contrastive loss weight λ')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--output', default='simulation_results.json')
    args = parser.parse_args()

    random.seed(args.seed)
    torch.manual_seed(args.seed)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    print("\n" + "="*60)
    print(f"Incremental Learning Simulation — IL EcoBin")
    print(f"T={args.T} cycles, N={args.N}/cycle, device={device}")
    print("="*60 + "\n")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    # Load model
    feature_extractor, model = load_model(args.checkpoint)
    feature_extractor = feature_extractor.to(device)
    model = model.to(device)

    # Load prototypes
    prototypes = torch.load(args.prototypes, map_location='cpu')

    # Eval dataset (tetap selama T cycle)
    eval_dataset = ImageFolder(root=args.eval_data, transform=transform)
    eval_loader = DataLoader(eval_dataset, batch_size=32, shuffle=False, num_workers=0)

    # Feedback dataset (dibagi per cycle)
    feedback_dataset = ImageFolder(root=args.feedback_data, transform=transform)
    total_indices = list(range(len(feedback_dataset)))
    random.shuffle(total_indices)
    cycle_size = min(args.N, len(total_indices) // args.T)
    print(f"[INFO] Feedback dataset: {len(feedback_dataset)} samples → {cycle_size}/cycle\n")

    # Tracking
    results = {}
    all_cycle_accs = []

    for t in range(args.T):
        print(f"{'─'*40}")
        print(f"Cycle {t+1}/{args.T}")

        # 1. Ambil N sample untuk cycle ini
        start = t * cycle_size
        end = start + cycle_size
        cycle_indices = total_indices[start:end]
        cycle_subset = Subset(feedback_dataset, cycle_indices)
        cycle_loader = DataLoader(cycle_subset, batch_size=min(32, len(cycle_indices)),
                                  shuffle=False, num_workers=0)

        # 2. Ekstrak fitur dari sample cycle ini
        cycle_features_by_class: Dict[str, List[torch.Tensor]] = defaultdict(list)
        idx_to_class = {v: k for k, v in feedback_dataset.class_to_idx.items()}

        with torch.no_grad():
            for images, labels in cycle_loader:
                images = images.to(device)
                feats = feature_extractor(images).squeeze(-1).squeeze(-1)
                for feat, lbl in zip(feats.cpu(), labels):
                    cls = idx_to_class[lbl.item()]
                    cycle_features_by_class[cls].append(feat)

        # 3. Update prototype per kelas yang ada feedback-nya
        for cls, feats in cycle_features_by_class.items():
            feat_tensor = torch.stack(feats)
            prototypes = update_prototype(prototypes, cls, feat_tensor, args.eta, args.h)
            print(f"  Updated prototype '{cls}' dengan {len(feats)} samples baru")

        # 4. Evaluasi akurasi setelah update
        cycle_accs = evaluate(model, eval_loader, device)
        all_cycle_accs.append(cycle_accs)
        avg_acc = sum(cycle_accs.values()) / len(cycle_accs)
        print(f"\n  Akurasi setelah cycle {t+1}: avg={avg_acc:.4f}")
        for cls, acc in cycle_accs.items():
            print(f"    {cls}: {acc:.4f}")

        results[f'cycle_{t+1}'] = cycle_accs

    # Hitung BWT
    if len(all_cycle_accs) >= 2:
        last = all_cycle_accs[-1]
        bwt_vals = []
        for i, acc_at_i in enumerate(all_cycle_accs[:-1]):
            for cls in CLASSES:
                bwt_vals.append(last.get(cls, 0) - acc_at_i.get(cls, 0))
        bwt = sum(bwt_vals) / len(bwt_vals)
    else:
        bwt = 0.0

    aia = sum(
        sum(cycle.values()) / len(cycle)
        for cycle in all_cycle_accs
    ) / len(all_cycle_accs)

    print("\n" + "="*60)
    print(f"HASIL SIMULASI:")
    print(f"  BWT: {bwt:.4f} {'(forgetting)' if bwt < 0 else '(no forgetting)'}")
    print(f"  AIA: {aia:.4f}")
    print("="*60 + "\n")

    results['summary'] = {
        'BWT': bwt,
        'AIA': aia,
        'T': args.T,
        'N': args.N,
        'eta': args.eta,
        'h': args.h,
        'gamma': args.gamma,
        'lambda': args.lam,
    }

    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"[OK] Hasil disimpan: {args.output}")

    # Simpan prototype terupdate
    proto_out = args.output.replace('.json', '_prototypes.pt')
    torch.save(prototypes, proto_out)
    print(f"[OK] Prototype terupdate disimpan: {proto_out}")


if __name__ == "__main__":
    main()
