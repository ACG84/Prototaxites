# Analysing the dinocyst spectral dataset

Meyvisch et al.'s **Table S2** obtained: **219 spectra × 2,379 wavenumbers (602–3996 cm⁻¹)** with full
metadata (taxon, order, family, colour, trophic preference, locality, water depth, spectrochemical
group), plus three reference standards.

| Group | n |
|---|---|
| coloured | 109 |
| transparent | 79 |
| aliphatic | 17 |
| aromatic | 6 |
| standards / averages | 8 |

**Standards included: Eumelanin (*Sepia officinalis*, Sigma M2649), microcrystalline Cellulose, and
*Pinus* pollen.** The eumelanin standard is the useful one — it is a **tyrosine-derived aromatic
biopolymer**, the compound class the aromatic-protein hypothesis proposes.

---

## Critical caveat on comparability

These spectra were baseline-corrected by the authors with a polynomial correction that leaves large
**negative** regions (dataset range −1.19 to +0.59; most groups are negative across 2900–1500 cm⁻¹).
**Absolute band intensities are therefore not comparable with Loron et al.'s values.** Only band
*positions*, spectral *shapes*, and *within-dataset* comparisons are valid here.

A sanity check confirms the extraction is sound: the cellulose standard shows the expected
polysaccharide profile — 1030 (0.386), 1100 (0.191), 1160 (0.109) cm⁻¹ — and is flat across
1500–1700.

---

## The eumelanin result

Mean absorbance at diagnostic wavenumbers:

| | 1660 | 1620 | 1600 | **1570** | **1540** | 1510 | 1030 |
|---|---|---|---|---|---|---|---|
| **Eumelanin standard** | 0.043 | 0.153 | 0.192 | **0.222** | **0.205** | 0.166 | −0.026 |
| Cellulose standard | 0.013 | 0.012 | 0.008 | 0.005 | 0.004 | 0.004 | 0.386 |
| dinocyst coloured | −0.002 | 0.035 | 0.031 | 0.020 | 0.002 | −0.031 | 0.037 |
| dinocyst transparent | −0.116 | −0.115 | −0.124 | −0.130 | −0.134 | −0.138 | 0.044 |
| dinocyst aliphatic | −0.075 | −0.080 | −0.089 | −0.101 | −0.105 | −0.112 | 0.021 |
| dinocyst aromatic | −0.067 | −0.119 | −0.130 | −0.144 | −0.106 | −0.029 | 0.063 |

**Eumelanin's absorption maximum across 1400–1800 cm⁻¹ falls at 1570 cm⁻¹**, with a broad strong band
spanning roughly 1620–1510 — the aromatic C=C, C=N and N–H region of the indole system, overlapping
the amide II position.

### What this means for the hypothesis

**A tyrosine-derived aromatic biopolymer produces strong absorption exactly where *P. taiti* is
weakest.** *P. taiti* has the lowest Amide II of any group in the Rhynie assemblage (0.0170 mean,
0.0040 median). Fresh eumelanin is the opposite: that region is its dominant feature.

So the melanin-like version of the aromatic-protein hypothesis has a problem. If the *Prototaxites*
wall were a melanin-type tyrosine polymer, the 1540–1570 region should be strong, and it is the single
weakest thing about the fossil's spectrum.

**But this does not close it**, for a reason Loron et al. supply themselves: melanin "is molecularly
similar to kerogen, meaning that even if present in the cell wall, its signal would be hidden by the
stronger general kerogen signal." The comparison here is a **modern standard against a 407 Ma fossil**,
and the fossilisation step is precisely what they say erases the signature.

The honest statement: the fresh polymer looks nothing like the fossil, so the hypothesis now requires
diagenesis to do **all** of the work — converting a material whose dominant band is at 1570 cm⁻¹ into
one with essentially no absorption there. That is a heavier load than the hypothesis carried before.

---

## A discrepancy I cannot resolve

Meyvisch et al. state that amide bands (their bands "1B–C" and "1E") are **ubiquitous in all
specimens**. In my windows, the **transparent** and **aliphatic** groups show *nothing* at 1540 — their
only positive features are the polysaccharide bands at 1030–1100, consistent with the "cellulose-like
backbone." Only the **coloured** group shows positive absorption in the amide region.

Their Table 1 band positions (1A–1G) did not survive text extraction from the PDF, so I cannot apply
their definitions. Possible explanations: their amide assignments sit at wavenumbers I did not sample;
the effect is visible in second-derivative rather than raw spectra; or the ubiquity claim rests on
weaker features than my flanking-baseline method retains.

**This matters for the earlier conclusion.** [`existing-analogues.md`](existing-analogues.md) §2b leaned
on "amide bands in all spectra" to argue that every protist resistant wall retains nitrogen. That claim
is the authors', and I cannot independently reproduce it from their own data for two of their four
groups. It should be reported as their interpretation rather than as a verified measurement.

---

## What would make this dataset fully usable

**Loron et al.'s table S1.** With their exact band definitions, the 219 dinocyst spectra could be
reduced to the same six features and projected into the published CCA — giving a protist resistant-wall
comparison group of n = 219 against the current n = 3. The baseline-correction mismatch would still
need handling (ratios rather than absolute intensities), but it is the single largest available
improvement to the comparison.

---

## Data

`Table S2` from Meyvisch et al. (2023), *J. Phycol.* 59:1064–1084, doi:10.1111/jpy.13382.
Loaded and cached as `dino.pkl` in the working directory; extraction code is straightforward xlsx
parsing (see `network-analysis/` for the pattern).
