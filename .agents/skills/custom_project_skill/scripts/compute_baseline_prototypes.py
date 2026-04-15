"""
compute_baseline_prototypes.py — Hitung prototype awal dari MobileNetV3-Large

Mengambil feature extractor dari mobilenetv3_MX150_best.pth dan menghitung:
- Mean vector µ_j per kelas (Han et al. 2024, Eq. 1)
- Bandwidth matrix H_j via Gaussian KDE (Han et al. 2024, Eq. 7)

Output: baseline_prototypes.pt — dictionary {class_name: {'mu': tensor, 'H': tensor}}

Usage:
    python scripts/compute_baseline_prototypes.py \
        --checkpoint mobilenetv3_MX150_best.pth \
        --dataset dataset_kating_cropped/valid \
        --output baseline_prototypes.pt
"""

import argparse
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from pathlib import Path
from collections import defaultdict


CLASSES = ['organic', 'recycle', 'residue', 'reusable']
FEATURE_DIM = 960  # MobileNetV3-Large output sebelum classifier head


def load_feature_extractor(checkpoint_path: str) -> nn.Module:
    """Load MobileNetV3-Large dan hapus classifier head → 960-dim output."""
    # Load full model (asumsi structure dari TrainingMobileNetV3_MX150.ipynb)
    model = models.mobilenet_v3_large(weights=None)
    num_classes = len(CLASSES)
    model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)

    checkpoint = torch.load(checkpoint_path, map_location='cpu')

    # Handle berbagai format checkpoint
    state_dict = checkpoint
    if 'model_state_dict' in checkpoint:
        state_dict = checkpoint['model_state_dict']
    elif 'state_dict' in checkpoint:
        state_dict = checkpoint['state_dict']

    model.load_state_dict(state_dict)

    # Hapus classifier head untuk mendapat 960-dim features
    feature_extractor = nn.Sequential(*list(model.children())[:-1])
    feature_extractor.eval()

    print(f"[OK] Feature extractor loaded dari: {checkpoint_path}")
    print(f"     Output dimension: {FEATURE_DIM}-dim")
    return feature_extractor


def extract_features(
    feature_extractor: nn.Module,
    dataset_path: str,
    batch_size: int = 32
) -> dict:
    """Ekstrak feature vector dari seluruh dataset, dikelompokkan per kelas."""
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    dataset = ImageFolder(root=dataset_path, transform=transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False, num_workers=0)

    class_to_features = defaultdict(list)
    idx_to_class = {v: k for k, v in dataset.class_to_idx.items()}

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    feature_extractor = feature_extractor.to(device)

    print(f"[INFO] Mengekstrak fitur dari: {dataset_path}")
    print(f"       Device: {device}, Total samples: {len(dataset)}")

    with torch.no_grad():
        for batch_idx, (images, labels) in enumerate(dataloader):
            images = images.to(device)
            features = feature_extractor(images)
            features = features.squeeze(-1).squeeze(-1)  # flatten adaptive avg pool output

            for feat, label in zip(features.cpu(), labels):
                class_name = idx_to_class[label.item()]
                class_to_features[class_name].append(feat)

            if (batch_idx + 1) % 10 == 0:
                print(f"       Batch {batch_idx+1}/{len(dataloader)} diproses")

    # Stack per kelas
    result = {}
    for cls, feats in class_to_features.items():
        result[cls] = torch.stack(feats)  # shape: (N_cls, 960)
        print(f"  Kelas '{cls}': {len(feats)} samples")

    return result


def compute_prototypes(class_features: dict, h: float = 0.5) -> dict:
    """
    Hitung mean vector µ_j dan bandwidth matrix H_j per kelas.

    Formula dari Han et al. (2024):
    - µ_j = (1/N_j) * Σ f_θ(x)         [Eq. 1]
    - H_j = h * (N_j - 1) / (X_j^T X_j) [Eq. 7]

    Args:
        class_features: dict {class_name: tensor (N, 960)}
        h: bandwidth hyperparameter (default: 0.5)

    Returns:
        dict {class_name: {'mu': tensor (960,), 'H': tensor (960, 960), 'N': int}}
    """
    prototypes = {}

    for cls, features in class_features.items():
        N = features.shape[0]
        mu = features.mean(dim=0)  # (960,)

        # Bandwidth matrix H_j = h * (N-1) / (X^T X)  [Han et al. Eq. 7]
        # Note: computed only over diagonal for efficiency (diagonal approximation)
        # Full matrix version: H = h * (N-1) * torch.inverse(features.T @ features)
        XtX = features.T @ features  # (960, 960)

        try:
            XtX_inv = torch.inverse(XtX)
            H = h * (N - 1) * XtX_inv
        except RuntimeError:
            # Fallback: pseudo-inverse jika singular (sering pada dataset kecil)
            XtX_inv = torch.linalg.pinv(XtX)
            H = h * (N - 1) * XtX_inv
            print(f"  [WARN] Kelas '{cls}': XtX singular, menggunakan pseudo-inverse")

        prototypes[cls] = {
            'mu': mu,
            'H': H,
            'N': N,
        }

        print(f"  Prototype '{cls}': µ shape={mu.shape}, H shape={H.shape}, N={N}")

    return prototypes


def main():
    parser = argparse.ArgumentParser(description="Hitung baseline prototypes IL EcoBin")
    parser.add_argument('--checkpoint', default='mobilenetv3_MX150_best.pth',
                        help='Path ke checkpoint MobileNetV3-Large')
    parser.add_argument('--dataset', default='dataset_kating_cropped/valid',
                        help='Path ke dataset split (train/valid/test)')
    parser.add_argument('--output', default='baseline_prototypes.pt',
                        help='Path output file prototype')
    parser.add_argument('--bandwidth', type=float, default=0.5,
                        help='Bandwidth hyperparameter h untuk KDE (default: 0.5)')
    parser.add_argument('--batch_size', type=int, default=32,
                        help='Batch size untuk feature extraction (default: 32)')
    args = parser.parse_args()

    print("\n" + "="*60)
    print("Compute Baseline Prototypes — IL EcoBin")
    print("="*60 + "\n")

    # Step 1: Load feature extractor
    feature_extractor = load_feature_extractor(args.checkpoint)

    # Step 2: Ekstrak fitur per kelas
    class_features = extract_features(feature_extractor, args.dataset, args.batch_size)

    # Step 3: Hitung prototypes
    print(f"\n[INFO] Menghitung prototypes (h={args.bandwidth})...")
    prototypes = compute_prototypes(class_features, h=args.bandwidth)

    # Step 4: Simpan
    output_path = Path(args.output)
    torch.save(prototypes, output_path)
    print(f"\n[OK] Prototypes disimpan ke: {output_path.resolve()}")

    # Tampilkan ringkasan
    print("\nRingkasan Prototype:")
    for cls, proto in prototypes.items():
        print(f"  {cls}: N={proto['N']}, µ norm={proto['mu'].norm():.4f}")


if __name__ == "__main__":
    main()
