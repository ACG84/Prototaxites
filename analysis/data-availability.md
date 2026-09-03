# Has anyone already collected the data we need?

An audit of what exists, what is downloadable, and what genuinely has to be generated.

**Headline: more exists than expected.** The 2026 study's feature matrix and full analysis pipeline
are public, so the CCA/SVM can be reproduced and extended today. The single most relevant
foraminiferal dataset was collected in 1997 and published in 2000, but only in print. The
xenophyophore gap is real.

---

## 1. The 2026 Prototaxites analysis — public, and usable

Data availability statement (Loron et al. 2026, verbatim):

> "All data are available in the main text or the Supplementary Materials. Codes used to produce this
> work were deposited in the Zenodo repository DOI: 10.5281/zenodo.17632257 after archiving them from
> the Github https://github.com/nrodgers1/Prototaxites-Analysis-code"

There is **no separate raw-spectra deposit for the 2026 paper** — unlike the 2023 study. But the
GitHub repository (772 KB, CC-BY-4.0) contains more than code:

| File | What it is |
|---|---|
| `CCA_final for revision_010725.xlsx` | **The CCA input matrix — all 102 samples** |
| `CCA_Vegan_Protaxities_version.ipynb` / `.html` | CCA via R `vegan` through `rpy2` |
| `PCA.py`, `DAPC.py`, `DAPC_smote.py` | Ordination and discriminant analysis |
| `SVM_smote.py`, `learning curve*.py` | The classifiers and learning curves |
| `Hotelling_T2_Q.py` | Outlier detection |

**The critical practical finding: the matrix has only six features.** Placing a new specimen into the
published space does not require raw spectra — it requires six normalised band intensities computed
the same way (band definitions in their table S1):

`N-products` · `Amide II` · `N-product and carboxylate` · `Amide I` · `CH2` · `CH3`

Sample counts confirm the composition reported in the text: Plant 37, Fungi 24, *Prototaxites* 12,
Arthropods 12, Bacteria 10, **Amoeba 3** (4 unlabelled rows).

### 1.1 What the amoeba control actually looks like

The three amoeba samples (`agl127 f47-3 testate`, `amoboa agl127 h38-4`, `amoboa agl127 k49-3`),
computed from the published matrix:

**Group means**

| Group | N-products | Amide II | N-prod+carboxylate | Amide I | CH2 | CH3 |
|---|---|---|---|---|---|---|
| Plant | 0.1886 | 0.0890 | 0.2211 | 0.4236 | 0.4047 | 0.1566 |
| **Prototaxites** | **0.1333** | **0.0170** | **0.1272** | **0.2771** | 0.2493 | 0.1179 |
| Fungi | 0.2300 | 0.1367 | 0.2219 | 0.5478 | 0.3883 | 0.1480 |
| Bacteria | 0.1316 | 0.0663 | 0.1836 | 0.4064 | 0.7095 | 0.3364 |
| Arthropods | 0.2645 | 0.1739 | 0.2364 | 0.5148 | 0.3842 | 0.1482 |
| **Amoeba** | **0.2564** | **0.1796** | **0.2536** | **0.5294** | 0.2316 | 0.0942 |

The amoeba has the **highest mean Amide II of any group in the dataset** — above arthropods (chitin +
protein) and above fungi. *Prototaxites* has by far the lowest: 0.0170, against a next-lowest of
0.0663 for bacteria. On the nitrogen bands the protist test and *Prototaxites* sit at opposite
extremes of the whole assemblage.

**Separation, honestly reported** (n = 3 for amoeba is doing a lot of work):

| Feature | *Prototaxites* max | Amoeba min | Verdict |
|---|---|---|---|
| **Amide I** | 0.3286 | 0.4327 | **Fully separated, no overlap** |
| Amide II | 0.1091 | 0.0876 | Overlaps at the extremes — but medians 0.0040 vs 0.2040 (~50×) |
| N-products | 0.2468 | 0.1687 | Overlaps — medians 0.1385 vs 0.2843 |

So the control is real and it points the way already described, but it is not bulletproof: only
Amide I separates cleanly, and two features overlap at their tails on a sample of three. **Anyone
wanting to lean on this control should say n = 3 out loud.** Strengthening it — more amoeba
specimens from the same thin sections — is cheap and would be worth doing before any rhizarian work.

---

## 2. The key foraminiferal study is freely downloadable — correcting an earlier note

An earlier version of this file said Allen et al. (2000) was print-only. **That was wrong.** The
Grzybowski Foundation hosts the IWAF-5 proceedings as open PDFs, and the paper is at:

**https://gf.tmsoc.org/Documents/IWAF-5/Allen+Roberts+Murray-IWAF5-1997.pdf**

> Allen K, Roberts S, Murray JW (2000). Analysis of organic components in the test wall of
> agglutinated foraminifera by Fourier Transform Infrared and Pyrolysis Gas Chromatography/Mass
> Spectrometry. In: Hart MB, Kaminski MA, Smart CW (eds), *Proceedings of the Fifth International
> Workshop on Agglutinated Foraminifera*, Grzybowski Foundation Special Publication **7**, 1–13.

### What it contains

**Specimens** — organic linings *and* tests, isolated:

| Taxon | Grade |
|---|---|
| ***Astrammina rara*** Rhumbler | **Monothalamid** astrorhizid, "the giant Antarctic foraminifera" |
| *Jadammina macrescens* (Brady) | Agglutinated marsh |
| *Trochammina inflata* Montagu | Agglutinated marsh |
| *Ammonia beccarii* (Linné) | Calcareous — lining only |

**Reference standards: chitin and collagen** (Sigma), run alongside. This is the crucial design
feature — it lets the foraminiferal material be placed against both candidate biopolymers directly.

**Techniques:** FT-IR over 4000–450 cm⁻¹ with Fourier self-deconvolution for protein secondary
structure, plus Py-GC/MS.

### Findings

> "Results from FT-IR and Py-GC/MS analysis of the organic materials in agglutinated foraminifera
> tests have highlighted the presence of protein and carbohydrate components, thus supporting earlier
> suggestions that the cement and lining material is **glycoproteinaceous**... the main part of the
> organic material exists as a **proteinaceous component, containing only minor amounts of
> carbohydrate**."

- FT-IR spectra and Py-GC/MS products were "strikingly" similar to **collagen**.
- Amide I secondary structure differs by taxon: ***A. rara* absorbs strongly at 1635 cm⁻¹** (β-sheet),
  while *J. macrescens* and *T. inflata* peak at **1652 cm⁻¹** (α-helix). Chitin reference sits at
  1660 and 1626 cm⁻¹.
- Protein pyrolysis products throughout: pyrrole (proline/hydroxyproline), toluene and styrene
  (phenylalanine), indole and methylindoles (tryptophan), phenols (tyrosine), and a **proline–proline
  2,5-diketopiperazine identified from *A. rara***.
- Carbohydrate indicators (furans: 2,3-dihydrobenzofuran, 2,4-dimethylfuran) present but **weak** —
  "the levels of carbohydrate moieties within the general structure are low."
- Long-chain hydrocarbons in all pyrograms indicate lipid. DeLaca (1986) put lipid at ~19% of *A. rara*
  shell composition, later questioned as pseudopodial contamination (Bowser & Bernhard 1993).

### An interpretive caution worth carrying forward

The paper flags something directly relevant to reading *Prototaxites*:

> "the observation of abundant phenol and methyl phenols **may not be specific for tyrosine** since
> these products may also originate from a **non-proteinaceous phenolic biopolymer**"

Phenolic pyrolysis products are ambiguous between protein and a phenolic biopolymer. Anyone arguing
from phenolic signal alone — in either direction — needs to say which.

### The limitation

**The bands Loron et al. use are all present** — amide I/II at 1660–1550, CH₂ at 2853/2925, CH₃ at
2873/2956, C=O at 1740/1750, polysaccharide C–O–C at 1000–1200. But the paper reports **band positions
and assignments plus spectra as figures**; Table 1 is secondary-structure assignments and Table 2a/b
are pyrolysis product lists. **No numeric absorbance intensities are tabulated.**

So the six normalised intensities cannot be computed directly from the published values. Options:
digitise the figures (lossy, but the amide bands are large and well separated), or approach the authors
— Stephen Roberts remains at Southampton — for original spectra, which after 25 years may not survive.

**What it does settle, without any of that:** the qualitative answer for the monothalamid grade, with
chitin and collagen as controls. Glycoproteinaceous, collagen-like, protein-dominated.

## 3. The 2023 comparative spectra — the only raw deposit

Loron et al. (2023), *Nat. Commun.* 14:1387 → **Edinburgh DataShare, doi:10.7488/ds/3806.**

Raw ATR-FTIR spectra for 49 Rhynie fossils, including the two *Palaeoleptochlamys hassii* specimens.
This is the only place raw spectra from either study are archived, and it is the right starting point
for anyone wanting to compute band intensities independently rather than trusting the derived matrix.

Physical material is locatable too: thin sections in the **Lyon Collection, University of Aberdeen**
(Lyon 156 UC1/UC2/UCB1, Lyon 48 UC1 — the uncovered sections used for FTIR), and NSC.36 sections plus
sub-blocks in **National Museums Scotland** (G.2024.5.1, G.2024.5.2). Blocks NSC.01–NSC.45 were
distributed via North Sea Core with NatureScot agreement.

---

## 4. Xenophyophores: the gap is real

- **No structural wall chemistry exists.** "Xenophyophore" does not appear once in Tyszka et al.'s
  2021 review of foraminiferal organic composition. The granellare sheath has been described
  morphologically and never characterised chemically.
- **Some biochemistry does exist, but the wrong kind:** lipid-class work by TLC-FID (fatty acids,
  sterols, triacylglycerols) used for *trophic ecology*, not wall structure. Descriptions mention
  "proteinaceous fibres" without analysis.
- **Specimens exist and are catalogued:** the Natural History Museum maintains a xenophyophore dataset
  (`data.nhm.ac.uk/dataset/xen`), and abyssal collections from CCZ nodule surveys are extensive.

So this is genuinely uncollected data, and it is collectable. It is also, unfortunately, the gap that
matters least — H1/H2 are already falsified in [`rhizaria-hypothesis.md`](rhizaria-hypothesis.md) on
xenophyae, stercomare, habitat and septation, so filling it changes no conclusion.

---

## 5. ForamL — an index, not a chemistry database

**Godos, Tyszka, Radmacher & Goleń (2021), Mendeley Data, doi:10.17632/xw7w5ns649.3** — 156
publications, 622 illustrated specimens of foraminiferal organic linings across the Phanerozoic,
assigned to supraordinal groups and chamber-arrangement types.

No composition data. But it is the right tool for **locating candidate control material**: it will
tell you which Paleozoic publications illustrate linings and from where, which is exactly the search
needed to find low-thermal-maturity Devonian assemblages (the binding constraint in
[`control-experiment.md`](control-experiment.md)).

---

## 6. Summary: collected vs. not

| Needed | Exists? | Where |
|---|---|---|
| 2026 CCA/SVM feature matrix (102 samples) | **Yes, public** | GitHub / Zenodo 10.5281/zenodo.17632257 |
| 2026 analysis pipeline | **Yes, public** | same |
| 2026 raw FTIR spectra | No separate deposit | "main text or Supplementary Materials" |
| Taphonomically matched protist control | **Yes, n = 3** | in the matrix above; raw at 10.7488/ds/3806 |
| FTIR/Py-GC-MS of monothalamid foram wall | **Yes — free PDF** (qualitative only, no numeric intensities) | [Allen et al. 2000](https://gf.tmsoc.org/Documents/IWAF-5/Allen+Roberts+Murray-IWAF5-1997.pdf) |
| Devonian foram lining occurrences | **Yes** | Bell & Winchester-Seeto 1999; ForamL |
| Devonian linings with *low* thermal maturity | Not identified | needs a targeted search via ForamL |
| FTIR of a *truly organic-walled* allogromiid (*Allogromia*) | **No** | not run by anyone; culturable material |
| Xenophyophore granellare wall chemistry | **No** | uncollected; specimens available |
| Physical Rhynie material for new FTIR | **Yes** | Lyon Collection (Aberdeen), NMS |

**The cheapest next step by a wide margin:** clone the analysis repo, reproduce the CCA from the
published matrix, and add more amoeba spectra from 10.7488/ds/3806 to take that control off n = 3.
That requires no lab, no loans, and no new specimens — and it either firms up the strongest existing
argument against a protist affinity or exposes it as resting on three samples.

---

## References

- Loron CC et al. (2026). *Sci. Adv.* 12(4):eaec6277. Code: https://github.com/nrodgers1/Prototaxites-Analysis-code
  · Zenodo doi:10.5281/zenodo.17632257 · Open-access text: https://aura.abdn.ac.uk/
- Loron CC et al. (2023). *Nat. Commun.* 14:1387. Raw spectra: Edinburgh DataShare doi:10.7488/ds/3806
- Allen K, Roberts S, Murray JW (2000). Grzybowski Foundation Special Publication 7, 1–13.
  **Free PDF:** https://gf.tmsoc.org/Documents/IWAF-5/Allen+Roberts+Murray-IWAF5-1997.pdf
  (Whole IWAF-5 volume: https://gf.tmsoc.org/Documents/IWAF-5/)
- Allen K, Roberts S, Murray JW (1999). *J. Micropalaeontol.* 18:183–191.
  https://jm.copernicus.org/articles/18/183/1999/jm-18-183-1999.pdf
- Godos K, Tyszka J, Radmacher W, Goleń J (2021). ForamL v1.2. Mendeley Data doi:10.17632/xw7w5ns649.3
- Bell KN, Winchester-Seeto TM (1999). *J. Micropalaeontol.* 18:27–43.
- NHM xenophyophore dataset: https://data.nhm.ac.uk/dataset/xen
