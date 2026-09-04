# The raw spectra: a clean qualitative result

Loron et al.'s **Data S1** obtained — the complete raw ATR-FTIR dataset. This supersedes every
inference in this repository that was made from their derived six-feature matrix.

## What the file contains

| Sheet | Content |
|---|---|
| **Raw spectra** | **102 spectra, 650.5–4000 cm⁻¹, 1798 points**, each labelled by group |
| D1–D5 (± outlier-removed) | Processed subsets, 1450.2–2999.1 cm⁻¹, 268 points |
| **CCA** | The six features, **with band numbers** |

Groups: Plant 33, Fungi 24, *Prototaxites* 12, Arthropod 12, Bacteria 10, Plant spore 4, Oomycete 4,
**Amoeba 3**.

Band identities are now pinned: N-products = band 12, **Amide II = band 11**, N-product+carboxylate =
band 10, **Amide I = band 7**, CH₂ = band 2, CH₃ = band 1.

A caution the raw data makes obvious: the **1030 cm⁻¹ region is dominated by Si–O of the chert
matrix**, an order of magnitude above any organic band. Any normalisation spanning it is normalising
to silica. Their processed D-sheets sensibly start at 1450 cm⁻¹.

---

## The result: *Prototaxites* has no resolved amide I peak
> **Further corrected in [`amide-crosscheck.md`](amide-crosscheck.md).** Tissue-level cross-checking
> shows the 1650 component appears in N-free plant cuticle, peaks in a *decayed* axis, and is scarce in
> chitinous fungal spores. It does not behave as a protein marker in this material, so the inference
> from its absence to absent protein is withdrawn.


> **Corrected in [`what-structure.md`](what-structure.md) §1.** Second-derivative analysis shows this
> is a *quantitative tendency*, not a categorical absence: 4/12 *Prototaxites* spectra do carry a
> 1638–1668 cm⁻¹ component, against 62–67% for the proteinaceous groups. The group-mean statement below
> holds; the "discrete presence/absence" framing does not.

Local maxima in 1500–1750 cm⁻¹, from the processed group-mean spectra:

| Group | Peaks (cm⁻¹, height) |
|---|---|
| **Amoeba** | 1614 (0.996), 1683 (0.534), **1651 (0.529)**, 1523 (0.342) |
| **Fungi** | 1614 (0.986), **1650 (0.550)**, 1683 (0.507), 1523 (0.323) |
| **Arthropod** | 1614 (0.991), 1683 (0.518), **1651 (0.515)**, 1523 (0.326) |
| ***Prototaxites*** | 1612 (0.998), 1687 (0.456), 1525 (0.326) — **no 1650 peak** |
| Plant | 1612 (0.994), 1683 (0.485), 1527 (0.302) — no 1650 peak |
| Bacteria | 1612 (0.995), 1683 (0.469), 1525 (0.282) — no 1650 peak |

**The amoeba, the fungi and the arthropods each resolve a distinct amide I maximum at 1650–1651 cm⁻¹.
*Prototaxites* does not. Nor do plants or bacteria.**

Every group shares a dominant band at 1612–1614 cm⁻¹, so that feature is **not** diagnostic — it is
common to organic and matrix alike. The discrimination is carried by whether a separate amide I
maximum resolves out of that envelope.

Band heights at the two amide positions:

| | 1650 | 1540 |
|---|---|---|
| Fungi | 0.5498 | 0.2300 |
| Amoeba | 0.5227 | 0.2564 |
| Arthropod | 0.5127 | 0.2645 |
| Plant | 0.4194 | 0.1866 |
| Bacteria | 0.4098 | 0.1316 |
| ***Prototaxites*** | **0.2864** | **0.1333** |

---

## Why this is stronger evidence than anything used so far

Previous arguments in this repository — mine and the paper's — rested on **multivariate separation**
across six correlated features, where I showed no single band discriminates
([`data-availability.md`](data-availability.md) §1.2). This is different: a **discrete, qualitative
presence/absence** of a resolved peak, visible in the group-mean spectra without any classifier.

The three groups with proteinaceous or chitinous walls all show it. *Prototaxites* groups instead with
plants and bacteria.

### What it does to the aromatic-protein hypothesis

**This is the hardest evidence against it yet.** Amide I is predominantly backbone C=O stretch. A
protein retains backbone carbonyl regardless of how heavily its side chains are cross-linked —
di-tyrosine coupling modifies side chains, not the peptide backbone. So a cross-linked structural
protein should still resolve an amide I maximum.

*Prototaxites* shows none, while three co-occurring organisms in the same chert, under the same
diagenesis, all do.

The escape routes remaining are narrower than before:

1. **Backbone loss with side-chain survival.** Peptide hydrolysis destroying the backbone while the
   cross-linked aromatic network persists. Chemically coherent — that is roughly what happens to
   sclerotised material — but it must explain why fungal and arthropod amide I survived alongside.
2. **Band broadening into the 1612 envelope** rather than true absence. Testable on the raw spectra by
   curve-fitting, which I have not attempted.

Both are now the whole hypothesis, and neither is supported by anything measured.

### And a caution that cuts the other way

*Prototaxites* is **not** distinguished from **plants** by this character — both lack the 1650 peak.
That is consistent with the paper's own CCA placement and with my earlier finding that
*Prototaxites*-vs-plant classification runs barely above baseline (0.800 vs 0.755). The amide I
absence separates *Prototaxites* from proteinaceous organisms; it does nothing to establish a new
lineage.

---

## Status of earlier claims in this repository

| Claim | Status |
|---|---|
| No single band discriminates *Prototaxites* from Fungi | **Stands** for the six derived features; the raw spectra show a qualitative amide I difference the features do not capture cleanly |
| Amide II falls ~2× harder than Amide I, indicating N–H modification | **Superseded.** With the raw spectra, the primary observation is the absence of a resolved amide I altogether, not a differential |
| Band definitions unknown | **Resolved** — band numbers now known; exact wavenumbers still require table S1 |

---

## Still outstanding

- **Table S1** for the exact wavenumber of each numbered band. The band *numbers* are now known from
  the CCA sheet, but not their positions.
- **Curve-fitting the 1500–1750 envelope** on the raw *Prototaxites* spectra, to distinguish a truly
  absent amide I from one broadened beyond resolution. This is the single most useful remaining
  analysis and needs no new data.
- **Molecular and mineral biomarker record of terrestrialization in the Rhynie Chert** (113 pp.) —
  received, not yet read.

## Data

Loron et al. (2026) *Sci. Adv.* 12(4):eaec6277, Data S1 (spectra) and Data S2 (specimen list:
Oxford University Museum, University of Aberdeen, National Museums of Scotland accessions).
Cached locally as `loron_raw.pkl` and `loron_d1.pkl`.
