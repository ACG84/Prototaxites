# Taphonomically matched FTIR: what exists, and what it shows

The recurring objection to every reference-matching exercise in this project has been that the
references are modern and the fossil is 407 Ma and silicified. This document is the search for
references that are **not** mismatched — same preservation, same age range — and what they turn out
to say.

---

## 1. What exists

| Source | Material | Age | Preservation | Obtained? |
|---|---|---|---|---|
| **Loron et al. 2023, Edinburgh DataShare** ([10283/4797](https://datashare.ed.ac.uk/handle/10283/4797)) | 49 Rhynie fossils + **4 blank chert** | 407 Ma | ATR, in situ, silicified | **yes, CC BY** |
| Loron et al. 2026, Sci Adv Data S1 | 102 Rhynie fossils | 407 Ma | as above | yes (already held) |
| **Igisu et al. 2009**, *Appl. Spectrosc.* 63:1112 | Bitter Springs prokaryotes | **~850 Ma** | **black chert**, in situ transmission | yes (PDF; band positions only) |
| Marshall et al. 2005, *Precambrian Res.* 138:208 | acritarchs, Roper / Ruyang / Tanana | 1.5 Ga – 565 Ma | macerated organic-walled | yes (PDF; band positions only) |
| Matsumura et al. 2016, *Palaeontology* 59:963 | *Spongiophyton* cuticle | **Middle Devonian** | compression, Paraná Basin | abstract only (publisher blocks) |
| Loron et al. 2022, *Vib. Spectrosc.* 123:103476 | Proterozoic organic-walled eukaryotes | Proterozoic | synchrotron FTIR | not reachable from here |
| Loron et al. 2026 DataShare ([10283/8961](https://datashare.ed.ac.uk/handle/10283/8961)) | *P. taiti* 3D models, images | — | — | inspected: **no spectra** |

Two things follow immediately. **Nobody deposits deep-time FTIR spectra** — of the papers above, only
the Rhynie work has machine-readable data. And **the 2023 deposit is the important one**: 47 of its 53
spectra are byte-identical to spectra in the 2026 dataset (r > 0.9999), so it is not new fossil data —
but the remaining four are **pure chert matrix**, measured on the same instrument, in the same
sessions, on the same thin sections. That is the mineral reference this project has been asking for
since [`feature-validation.md`](feature-validation.md).

It also supplies specimen filenames (thin section + England finder coordinate) for 47 of the 102
spectra, which Data S1 does not carry.

---

## 2. How much of a Rhynie spectrum is chert?

| Group | n | r with blank chert |
|---|---|---|
| Amoeba | 3 | 0.9746 |
| Arthropod | 12 | 0.9739 |
| Bacteria | 10 | 0.9728 |
| Fungi | 24 | 0.9752 |
| Oomycete | 4 | 0.9705 |
| Plant | 33 | 0.9732 |
| Plant spore | 4 | 0.9728 |
| ***Prototaxites*** | **12** | **0.9748** |

Mean r² with blank chert across all 102 spectra: **0.948**. Kruskal–Wallis across the eight groups
p = 0.211; *Prototaxites* against the rest p = 0.222.

Two readings, both worth having. Roughly **95% of the variance in every raw spectrum is silica** — and
***Prototaxites* is not anomalously matrix-dominated**, which removes one trivial explanation for its
distinctness. Whatever separates it is in the residual few per cent, not in how much rock was in the
beam.

---

## 3. The null test

Igisu et al. subtracted a *local* quartz-matrix spectrum from each microfossil spectrum, and validated
it with the obvious control: matrix minus matrix, which in their material showed no bands between
2300 and 1300 cm⁻¹. Running the same control here, with the same subtraction used on the fossils:

| blank − blank | amplitude (ptp, 1350–1800) | apparent "bands" |
|---|---|---|
| j11 − o10 | 0.0300 | 1370, 1387, 1411, 1430, 1609 |
| j11 − v26 | 0.0564 | 1372, 1409, 1428, 1594, 1607 |
| j11 − x25 | 0.0108 | **1543, 1612, 1648**, 1717, 1786 |
| o10 − v26 | 0.0151 | 1376, 1407, 1428, 1588, 1607 |
| v26 − j11 | 0.0241 | **1651**, 1698, 1719, 1737, 1763 |
| x25 − o10 | 0.0353 | 1364, 1411, 1465, 1478, **1534** |
| x25 − v26 | 0.0628 | 1366, 1409, 1428, 1446, 1465 |

against the matrix-corrected **fossils**:

| Group | amplitude | bands |
|---|---|---|
| Bacteria | 0.0243 | 1370, 1411, 1428, 1463, 1607 |
| Amoeba | 0.0184 | 1370, 1430, 1463, **1540**, 1609 |
| Arthropod | 0.0208 | 1372, 1428, 1463, **1540**, 1609 |
| Fungi | 0.0217 | 1370, 1428, 1463, **1540**, 1609 |
| Plant | 0.0221 | 1370, 1411, 1428, 1463, 1607 |
| ***Prototaxites*** | 0.0205 | 1372, 1411, 1428, 1480, 1609 |

**The null spans 0.0104–0.0628; every fossil group mean falls inside it.** And the bands the null
produces — 1370, 1409, 1428, 1446–1478, 1527–1543, 1588–1612, 1648–1651 — are the complete list of
bands recovered from the fossils, including the 1540 band at the amide II position and the 1607–1609
aromatic band.

Subtracting one blank piece of Rhynie chert from another reproduces every feature I recovered from the
fossils. **Matrix-corrected band positions in 1350–1800 cm⁻¹ are not interpretable in this material.**

Two independent lines say why. The correction is unstable: refitting the matrix coefficient on
650–1000 cm⁻¹ instead of 650–900 + 1800–2700 **flips the sign of every band area** (amide II goes from
−0.14…−0.06 to +0.35…+0.76) and scrambles the group ordering. And Igisu et al. identify quartz
overtone and combination bands in chert at **1995, 1870, 1793, 1684, 1610, 1525 and 1492 cm⁻¹** —
i.e. directly beneath amide I, the aromatic C=C band, and amide II.

---

## 4. What matched-preservation organic matter actually looks like

| Source | Age | Host | Bands after matrix subtraction |
|---|---|---|---|
| Igisu et al., Bitter Springs prokaryotes | 850 Ma | black chert | 2960, 2920, 2850; 1585; 1450; 1370 |
| Marshall et al., acritarchs | 1.5 Ga–565 Ma | macerated | 2960, 2920, 2850; 1710; 1600; 1450; 1355 |
| Matsumura et al., *Spongiophyton* | Mid-Devonian | compression | strong 3000–2800; 1800–1600 |
| this analysis, Rhynie group means | 407 Ma | chert | 1607–1609; 1463; 1428; 1370 |

The same four- or five-band skeleton every time: aliphatic C–H, one aromatic band near 1600, a CH₂/CH₃
pair near 1450 and 1370. **No amide bands are reported in any of them** — including Igisu's
prokaryotes, which were originally protein-rich, and whose subtraction passed the null test that the
Rhynie subtraction fails.

Set against the [Kimmel maturation series](../spectral-library/README.md): fossil collagen at
>50,000 BP still shows amide I at 1651 and amide II at 1545. Amide bands survive 50 kyr of burial
intact and are gone by 407 Ma in chert. The loss is real, it is not gradual band-shifting, and it
applies to material of known protein content.

---

## 5. Where blank chert falls in the fossil spectral space

Processing the four blanks exactly as the fossils (rubberband baseline, min–max, 1450–3000 cm⁻¹) and
projecting them into a PCA of the 102 fossil spectra:

* Mahalanobis distance to the fossil centroid: fossils median 2.04, max 6.62; **blank chert 1.98, 2.52,
  4.09, 4.10.** Two of the four blanks are closer to the centre of the fossil cloud than the median
  fossil.
* On the axis that separates *Prototaxites* from Fungi (LDA on PCA scores; the two-group classifier
  reaches 0.960 ± 0.076 on full spectra, baseline 0.667): Fungi span −3.51 to +1.04, *Prototaxites*
  +0.82 to +3.23, and **all four blanks fall at −0.96 to +0.05 — inside the Fungi range, outside the
  *Prototaxites* range.**

**Stated against itself:** in the full spectral space the blanks are *not* indistinguishable from
fossils — their nearest-fossil distances are 2.38–3.29, against a fossil-to-fossil nearest-neighbour
median of 0.99. Blank chert is a recognisably different spectrum. But it is not out of distribution,
and it projects onto the discriminant where the fungi are.

### What the axis tracks

| | Spearman ρ with LD1 | p |
|---|---|---|
| r with blank chert (matrix fraction) | −0.079 | 0.65 |
| **aliphatic C–H stretch area, 2800–3000** | **−0.460** | **0.005** |

| | C–H area |
|---|---|
| Fungi | +0.2511 |
| ***Prototaxites*** | **+0.1309** (p = 0.006) |

The discriminant is **not** driven by how much chert is in the beam — that objection fails. It *is*
driven by aliphatic content, and *Prototaxites* has about **half the aliphatic C–H of the co-occurring
fungi**. That is a robust chemical difference, measured on raw spectra without any matrix correction,
and it does not depend on any of the unstable machinery above.

---

## 6. Where this leaves things

**Strengthened.** *Prototaxites* is genuinely chemically distinct from the co-occurring fungi, in the
same rock, and the distinction survives the controls: it is not a matrix-fraction artifact, and it is
measurable in the C–H stretch region, which is far from the quartz overtones. Loron et al. are
detecting something real.

**Weakened.** The *identification* of that difference as nitrogen chemistry. The bands that would
carry it — amide I near 1650, amide II near 1540 — sit on quartz overtones at 1684 and 1525, cannot be
recovered above a blank-minus-blank null, and are absent from every other chert-hosted fossil anyone
has measured, including originally proteinaceous ones. What is measurable is that *Prototaxites* is
aliphatic-poor. "Aliphatic-poor" is not "chitin-free".

**Unchanged.** None of this bears on whether *Prototaxites* was a rhizarian. It bears on how much
weight the chemistry can carry for anybody's hypothesis, including
[H3′](allogromiid-hypothesis.md) and [H4](rhizaria-hypothesis.md).

**What would settle it.** The measurement that is missing is not another library. It is the blank —
and now that blank chert exists in the public record, the useful next step for anyone with the
instrument is the local one Igisu et al. did: matrix spectra taken *microns from each fossil in the
same section*, not four from one block, with the null test reported.

## Reproducing

```
cd matched-preservation
python3 blank_chert.py loron2023.pkl loron_raw.pkl
```
