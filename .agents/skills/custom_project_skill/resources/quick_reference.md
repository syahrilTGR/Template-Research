# Quick Reference — IL EcoBin

Cheatsheet cepat untuk sesi kerja. Baca ini + handoff.md sebelum mulai.

---

## Kelas (TETAP, tidak berubah)
```
organic | recycle | residue | reusable
```

## File-File Kunci

| File | Lokasi | Saat Dibutuhkan |
|---|---|---|
| Checkpoint klasifier | `mobilenetv3_MX150_best.pth` | Load model untuk Stage 3 |
| Deteksi YOLO | `waste_detection_v12/weights/best.pt` | Inference pipeline |
| Prototype awal | `baseline_prototypes.pt` (dibuat saat Stage 3) | IL update |
| Dataset baseline | `dataset_kating_cropped/` | Hitung prototype awal |
| Incremental data | `dataset_incremental_simulation/` | Simulasi IL cycle |

---

## Formula Kunci (Han et al. 2024)

### Mean Vector (Eq. 1)
$$\mu_{t-1,j} = \frac{1}{N_{t-1,j}} \sum_{i=1}^{N_{t-1,j}} F_\theta(x)$$

### Prototype Enhancement (Eq. 2)
$$p^{(i)}_{t-1,j} = \mu_{t-1,j} + \eta \cdot d^{(i)}_{t-1,j} \cdot e$$

### Bandwidth Matrix KDE (Eq. 7)
$$H^{(j)}_{t-1} = h \cdot \frac{N_{t-1,j} - 1}{(X^{(j)}_{t-1})^T X^{(j)}_{t-1}}$$

### Contrastive Feature Loss (Eq. 10)
$$\min_{\theta_t} L_{C,t} = \| \Omega_t - \Omega_{t-1} \|$$

### Total Integration Loss (Eq. 13)
$$\{\theta_t, \phi_t\} = \arg\min_{\theta_t, \phi_t} \{ L_t + \gamma L_{P,t} + \lambda L_{C,t} \}$$

---

## Hyperparameter Awal

| Param | Nilai |
|---|---|
| η | 0.1 |
| h | 0.5 |
| γ | 0.5 |
| λ | 0.1 |
| τ | 0.70–0.80 |
| Feature dim | 960 |
| T cycles | 5–10 |
| N per cycle | 20–50 |

---

## Metrik Forgetting

| Metrik | Formula | Interpretasi |
|---|---|---|
| BWT | `(1/(T-1)) Σ(R_T,i - R_i,i)` | < 0 = forgetting |
| AIA | `mean accuracy semua cycle` | Makin tinggi makin baik |

---

## Checklist Stage 3 (Cepat)

- [ ] Load backbone 960-dim (freeze)
- [ ] Hitung µ_j, H_j baseline
- [ ] Loop T cycles: update prototype → loss → eval
- [ ] Plot BWT/AIA curve
- [ ] Export ONNX
