"""
evaluate_forgetting.py — Hitung metrik forgetting untuk IL evaluation

Menghitung:
- BWT (Backward Transfer): seberapa banyak forgetting terjadi
- FWT (Forward Transfer): seberapa banyak transfer positif ke task baru  
- AIA (Average Incremental Accuracy): rata-rata akurasi lintas semua cycle

Formula BWT (dari deepdive_incremental_learning.md):
    BWT = (1/(T-1)) * Σ_{i=1}^{T-1} (R_{T,i} - R_{i,i})
    - R_{T,i}: akurasi pada task i setelah training full T tasks
    - R_{i,i}: akurasi pada task i tepat setelah training task i

Usage:
    from scripts.evaluate_forgetting import ForgettingTracker
    
    tracker = ForgettingTracker(num_cycles=T)
    for t in range(T):
        # Setelah training cycle t:
        tracker.record(cycle=t, accuracies={class: acc for class, acc in ...})
    
    tracker.report()
    tracker.plot()
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, List, Optional


CLASSES = ['organic', 'recycle', 'residue', 'reusable']


class ForgettingTracker:
    """
    Melacak akurasi per kelas di setiap incremental cycle dan
    menghitung metrik forgetting.
    
    Matrix R[t][i] = akurasi pada task/kelas i setelah cycle t
    """

    def __init__(self, num_cycles: int, classes: List[str] = CLASSES):
        self.num_cycles = num_cycles
        self.classes = classes
        # R[t][cls] = akurasi kelas cls setelah cycle t
        self.R: Dict[int, Dict[str, float]] = {}

    def record(self, cycle: int, accuracies: Dict[str, float]) -> None:
        """
        Catat akurasi per kelas setelah cycle tertentu.
        
        Args:
            cycle: nomor cycle (0-indexed)
            accuracies: {kelas: akurasi (0.0 - 1.0)}
        """
        self.R[cycle] = accuracies
        avg = np.mean(list(accuracies.values()))
        print(f"[Cycle {cycle}] Avg accuracy: {avg:.4f}")
        for cls in self.classes:
            acc = accuracies.get(cls, 0.0)
            print(f"  {cls}: {acc:.4f}")

    def compute_bwt(self) -> float:
        """
        Backward Transfer (BWT).
        BWT < 0 → forgetting terjadi
        BWT = 0 → tidak ada forgetting
        """
        T = len(self.R) - 1  # index cycle terakhir
        if T < 1:
            print("[WARN] Minimal 2 cycle diperlukan untuk BWT")
            return 0.0

        bwt_values = []
        for i in range(T):
            for cls in self.classes:
                R_Ti = self.R[T].get(cls, 0.0)  # akurasi kelas cls di akhir
                R_ii = self.R[i].get(cls, 0.0)  # akurasi kelas cls tepat setelah cycle i
                bwt_values.append(R_Ti - R_ii)

        bwt = np.mean(bwt_values)
        return float(bwt)

    def compute_aia(self) -> float:
        """Average Incremental Accuracy (AIA) — rata-rata akurasi semua cycle."""
        all_accs = []
        for cycle_accs in self.R.values():
            avg = np.mean(list(cycle_accs.values()))
            all_accs.append(avg)
        return float(np.mean(all_accs))

    def report(self) -> Dict[str, float]:
        """Tampilkan laporan metrik forgetting."""
        bwt = self.compute_bwt()
        aia = self.compute_aia()

        print("\n" + "="*50)
        print("FORGETTING EVALUATION REPORT")
        print("="*50)
        print(f"  BWT (Backward Transfer) : {bwt:.4f}")
        if bwt < -0.05:
            print("    ⚠️  Significant forgetting detected!")
        elif bwt < 0:
            print("    ⚠️  Slight forgetting — monitor closely")
        else:
            print("    ✅  No forgetting (BWT >= 0)")
        
        print(f"  AIA (Avg Incremental Acc): {aia:.4f}")
        print("="*50 + "\n")

        return {'BWT': bwt, 'AIA': aia}

    def plot(self, save_path: Optional[str] = None) -> None:
        """Plot accuracy per kelas vs incremental cycle."""
        cycles = sorted(self.R.keys())
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle('Incremental Learning — Forgetting Analysis', fontsize=14)

        # Plot 1: Accuracy per kelas vs cycle
        ax1 = axes[0]
        colors = ['#2196F3', '#4CAF50', '#FF5722', '#9C27B0']
        for cls, color in zip(self.classes, colors):
            accs = [self.R[t].get(cls, 0.0) for t in cycles]
            ax1.plot(cycles, accs, marker='o', label=cls, color=color)
        
        ax1.set_xlabel('Incremental Cycle')
        ax1.set_ylabel('Accuracy')
        ax1.set_title('Per-Class Accuracy per Cycle')
        ax1.set_ylim(0, 1.05)
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Plot 2: Average accuracy vs cycle
        ax2 = axes[1]
        avg_accs = [np.mean(list(self.R[t].values())) for t in cycles]
        ax2.plot(cycles, avg_accs, marker='s', color='black', linewidth=2)
        ax2.fill_between(cycles, avg_accs, alpha=0.1, color='gray')
        ax2.set_xlabel('Incremental Cycle')
        ax2.set_ylabel('Average Accuracy')
        ax2.set_title(f'Average Incremental Accuracy (AIA={self.compute_aia():.4f})')
        ax2.set_ylim(0, 1.05)
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"[OK] Plot disimpan ke: {save_path}")
        else:
            plt.show()

    def save_to_json(self, path: str = "forgetting_results.json") -> None:
        """Simpan semua hasil ke JSON untuk referensi."""
        output = {
            'per_cycle_accuracy': {str(t): accs for t, accs in self.R.items()},
            'metrics': self.report()
        }
        with open(path, 'w') as f:
            json.dump(output, f, indent=2)
        print(f"[OK] Hasil disimpan ke: {path}")


# ─── Quick demo ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Simulasi 5 cycle dengan nilai dummy untuk testing
    tracker = ForgettingTracker(num_cycles=5)

    # Simulasi: akurasi sedikit menurun seiring cycle (forgetting ringan)
    base = {'organic': 0.99, 'recycle': 0.98, 'residue': 0.97, 'reusable': 0.98}
    for t in range(5):
        accs = {cls: max(0.5, base[cls] - t * 0.01 + (0.005 * t)) for cls in CLASSES}
        tracker.record(cycle=t, accuracies=accs)

    tracker.report()
    tracker.plot(save_path='forgetting_curve_demo.png')
    tracker.save_to_json('forgetting_results_demo.json')
