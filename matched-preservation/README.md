# Matched-preservation data

`loron2023.pkl` — the 53 raw ATR-FTIR spectra from Loron et al. 2023 (*Nat Commun* 14:1387),
downloaded from [Edinburgh DataShare 10283/4797](https://datashare.ed.ac.uk/handle/10283/4797)
(CC BY 4.0) and parsed from `ATR_raw_spectra_Loronetal.xlsx`. Dict of `{'wn', 'S', 'names'}`;
53 × 1798 points on the same 650.5–4000.0 cm⁻¹ grid as the 2026 Data S1 spectra.

**Four of the 53 are pure chert matrix** (`agl2 j11_4 matrix`, `o10_4`, `v26_4`, `x25`) — the same
instrument, sessions and thin sections as the fossils. They are the only blank in the public record
for this material.

47 of the other 49 are byte-identical to spectra in the 2026 dataset (r > 0.9999), and supply
specimen filenames — thin section number plus England finder coordinate — that Data S1 lacks.

`blank_chert.py` — three controls run on those blanks: matrix fraction per fossil group, the
matrix-minus-matrix null test, and where blank chert falls in the fossil spectral space and on the
*Prototaxites*/Fungi discriminant. Results and interpretation in
[`../analysis/matched-preservation.md`](../analysis/matched-preservation.md).

Needs `loron_raw.pkl` (the 2026 Data S1 spectra sheet, `{'wn', 'S', 'labels'}`) alongside it.
