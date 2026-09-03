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

## 2. The most relevant foraminiferal dataset already exists — in print only

**Allen K, Roberts S, Murray JW (2000).** "Analysis of organic components in the test wall of
agglutinated foraminifera by Fourier transform infrared and pyrolysis gas chromatography/mass
spectrometry." In: Hart MB, Kaminski MA, Smart CW (eds), *Proceedings of the Fifth International
Workshop on Agglutinated Foraminifera* (Plymouth, September 1997), **Grzybowski Foundation Special
Publication 7**.

This is as close to a direct hit as the literature offers: **FTIR and Py-GC-MS of the organic
components of agglutinated foraminiferal test walls**, including the monothalamid astrorhizid
***Astrammina rara***. Same technique class as Loron et al.

Its companion paper — Allen, Roberts & Murray (1999), *J. Micropalaeontol.* 18:183–191, which **is**
free at Copernicus — points to it explicitly: *"A detailed description of the organic component
analysis is given in Allen et al. (in press)."* The 1999 paper covers the mineral phases (α-quartz,
clays, anatase in *Ammobaculites balkwilli*) by EDS, micro-laser Raman and FTIR, on material from
Swanwick and Warsash, Southampton.

**Status:** not freely downloadable. Grzybowski Foundation Special Publications circulate as print
volumes and scattered institutional PDFs (several SP7 chapters are on UCL Discovery). Obtaining it is
an interlibrary-loan problem, not a research problem.

**Caveat before getting excited:** 25-year-old published spectra are figures, not archived numeric
data, and the six band intensities Loron et al. use would have to be re-derived — possibly not
possible from printed plots. Its real value is qualitative: it already establishes the answer
(glycoproteinaceous, collagen-like) for the exact grade at issue.

---

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
| FTIR/Py-GC-MS of monothalamid foram wall | **Yes — but print only** | Allen et al. 2000, Grzybowski SP7 |
| Devonian foram lining occurrences | **Yes** | Bell & Winchester-Seeto 1999; ForamL |
| Devonian linings with *low* thermal maturity | Not identified | needs a targeted search via ForamL |
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
- Allen K, Roberts S, Murray JW (2000). Grzybowski Foundation Special Publication 7.
- Allen K, Roberts S, Murray JW (1999). *J. Micropalaeontol.* 18:183–191.
  https://jm.copernicus.org/articles/18/183/1999/jm-18-183-1999.pdf
- Godos K, Tyszka J, Radmacher W, Goleń J (2021). ForamL v1.2. Mendeley Data doi:10.17632/xw7w5ns649.3
- Bell KN, Winchester-Seeto TM (1999). *J. Micropalaeontol.* 18:27–43.
- NHM xenophyophore dataset: https://data.nhm.ac.uk/dataset/xen
