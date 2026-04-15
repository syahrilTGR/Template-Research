"""
check_dataset.py — Validasi dataset untuk proyek IL EcoBin

Fungsi:
1. Hitung jumlah sample per kelas
2. Deteksi file gambar yang corrupt atau tidak dapat dibuka
3. Tampilkan distribusi kelas (class imbalance check)

Usage:
    python scripts/check_dataset.py --dataset dataset_kating_cropped
    python scripts/check_dataset.py --dataset dataset_incremental_simulation
"""

import os
import sys
import argparse
from pathlib import Path
from PIL import Image
from collections import defaultdict


VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
CLASSES = ['organic', 'recycle', 'residue', 'reusable']


def check_dataset(dataset_dir: str) -> None:
    dataset_path = Path(dataset_dir)

    if not dataset_path.exists():
        print(f"[ERROR] Dataset direktori tidak ditemukan: {dataset_dir}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"Dataset: {dataset_path.resolve()}")
    print(f"{'='*60}\n")

    # Cek apakah ada split (train/valid/test) atau langsung kelas
    subdirs = [d for d in dataset_path.iterdir() if d.is_dir()]
    splits = [d.name for d in subdirs if d.name in ('train', 'valid', 'test')]

    if splits:
        scan_targets = [(split, dataset_path / split) for split in splits]
    else:
        scan_targets = [('root', dataset_path)]

    total_all = 0

    for split_name, split_path in scan_targets:
        print(f"--- Split: {split_name} ---")
        class_counts = defaultdict(int)
        corrupt_files = []
        unknown_classes = set()

        for class_dir in split_path.iterdir():
            if not class_dir.is_dir():
                continue
            class_name = class_dir.name
            if class_name not in CLASSES:
                unknown_classes.add(class_name)
                continue

            for img_file in class_dir.iterdir():
                if img_file.suffix.lower() not in VALID_EXTENSIONS:
                    continue
                try:
                    with Image.open(img_file) as img:
                        img.verify()
                    class_counts[class_name] += 1
                except Exception:
                    corrupt_files.append(str(img_file))

        total_split = sum(class_counts.values())
        total_all += total_split

        for cls in CLASSES:
            count = class_counts.get(cls, 0)
            bar = '█' * (count // 50)
            print(f"  {cls:10s}: {count:5d} {bar}")

        print(f"  {'TOTAL':10s}: {total_split:5d}")

        if unknown_classes:
            print(f"\n  [WARN] Kelas tidak dikenal ditemukan: {unknown_classes}")
            print(f"         Kelas yang valid: {CLASSES}")

        if corrupt_files:
            print(f"\n  [WARN] {len(corrupt_files)} file corrupt ditemukan:")
            for f in corrupt_files[:10]:
                print(f"         {f}")
            if len(corrupt_files) > 10:
                print(f"         ... dan {len(corrupt_files)-10} lainnya")
        else:
            print(f"\n  ✅ Tidak ada file corrupt.")
        print()

    print(f"\n  GRAND TOTAL: {total_all} gambar\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validasi dataset IL EcoBin")
    parser.add_argument(
        '--dataset',
        default='dataset_kating_cropped',
        help="Path ke direktori dataset (default: dataset_kating_cropped)"
    )
    args = parser.parse_args()

    check_dataset(args.dataset)
