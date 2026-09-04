# Do the six features track composition? A validation against known tissues

The Rhynie assemblage contains cutin, lignin, chitin, cellulose and protein-rich tissues in one
diagenetic setting. Data S2 identifies them per specimen. That allows a direct test: **do Loron et
al.'s six discriminating features behave as their names claim?**

Using **their** feature values (Data S1, CCA sheet) — not my band windows — joined to tissue type by
specimen number. Row order verified against the spectra sheet.

---

## The features, by tissue of known composition

| Tissue | n | N-products | **Amide II** | N-prod+carbox | **Amide I** | CH₂ | CH₃ |
|---|---|---|---|---|---|---|---|
| **cuticle — CUTIN, N-free** | 4 | 0.2254 | **0.1128** | 0.2537 | 0.4214 | 0.4746 | 0.1793 |
| **tracheid/conducting — LIGNIN, N-free** | 7 | 0.2567 | **0.1319** | 0.2812 | 0.4344 | 0.6075 | 0.2252 |
| plant axis / cortex | 19 | 0.1558 | 0.0644 | 0.1908 | 0.3989 | 0.3460 | 0.1362 |
| plant decayed axis | 1 | 0.3067 | 0.2116 | 0.2077 | 0.6490 | 0.3759 | 0.1676 |
| **glomeromycotan spores — CHITIN** | 4 | 0.2856 | 0.1435 | 0.2784 | 0.3949 | 0.3407 | 0.1165 |
| **fungal hyphae — CHITIN** | 3 | 0.0881 | **0.0070** | 0.2104 | 0.4279 | 0.3016 | 0.1058 |
| *Palaeomyces* — CHITIN | 16 | 0.2327 | 0.1507 | 0.2043 | 0.6108 | 0.4122 | 0.1635 |
| cyanobacteria — PROTEIN-rich | 10 | 0.1316 | 0.0663 | 0.1836 | 0.4064 | 0.7095 | 0.3364 |
| arthropod — CHITIN + PROTEIN | 12 | 0.2645 | 0.1739 | 0.2364 | 0.5148 | 0.3842 | 0.1482 |
| amoeba — PROTEINACEOUS test | 3 | 0.2564 | 0.1796 | 0.2536 | 0.5294 | 0.2316 | 0.0942 |
| ***Prototaxites* body tubes** | 7 | 0.1156 | **0.0026** | 0.1332 | 0.2530 | 0.3201 | 0.1539 |
| ***Prototaxites* medullary spots** | 5 | 0.1580 | 0.0373 | 0.1189 | 0.3109 | 0.1502 | 0.0675 |

---

## The validation test

Pooling **N-free reference tissues** (cutin + lignin, n = 11) against **N-bearing reference tissues**
(chitin + protein: spores, hyphae, *Palaeomyces*, cyanobacteria, arthropod, amoeba, n = 48). A feature
named for nitrogen should be higher in the N-bearing set.

| Feature | N-free | N-bearing | difference | Mann-Whitney p | verdict |
|---|---|---|---|---|---|
| N-products | 0.2453 | 0.2164 | **−0.0289** | 0.66 | **wrong direction** |
| Amide II | 0.1250 | 0.1311 | +0.0062 | 0.91 | no separation |
| N-product + carboxylate | 0.2712 | 0.2177 | **−0.0535** | 0.058 | **wrong direction** |
| Amide I | 0.4297 | 0.5097 | +0.0800 | 0.18 | no separation |
| CH₂ | 0.5592 | 0.4430 | −0.1162 | 0.20 | no separation |
| CH₃ | 0.2085 | 0.1838 | −0.0247 | 0.41 | no separation |

**Not one of the four nitrogen-named features separates nitrogen-bearing from nitrogen-free tissues.
Two run backwards.**

Concretely: **plant cuticle — cutin, a nitrogen-free polyester — scores Amide II = 0.1128, sixteen
times higher than chitinous fungal hyphae at 0.0070.** Lignified tracheids score higher still (0.1319).

---

## The sharpest consequence

The feature that most separates *Prototaxites* from Fungi is Amide II. Broken down by fungal structure:

| | n | Amide II | range |
|---|---|---|---|
| *Palaeomyces* | 16 | 0.1507 | 0.0000–0.4094 |
| Glomeromycotan spores | 4 | 0.1435 | 0.0724–0.2128 |
| **Fungal hyphae** | 3 | **0.0070** | 0.0007–0.0133 |
| ***Prototaxites* body tubes** | 7 | **0.0026** | 0.0003–0.0059 |

**Chitinous fungal hyphae and *Prototaxites* body tubes are indistinguishable on Amide II**
(p = 0.267). The Fungi group's Amide II signal comes from *Palaeomyces* and spores; the hyphae — the
most straightforwardly chitinous structures in the dataset — sit at *Prototaxites* levels.

**In fairness, they are not indistinguishable overall.** *Prototaxites* body tubes are significantly
lower than hyphae on two features:

| feature | *Prototaxites* body | hyphae | p |
|---|---|---|---|
| N-product + carboxylate | 0.1332 | 0.2104 | **0.017** |
| Amide I | 0.2530 | 0.4279 | **0.017** |
| N-products | 0.1156 | 0.0881 | 0.067 |
| Amide II | 0.0026 | 0.0070 | 0.267 |

So a real difference from hyphae exists — but not on the amide II feature, and not in a way that
supports "chitin present in fungi, absent in *Prototaxites*" as the explanation.

---

## What could explain the validation failure

Four possibilities, and they are not mutually exclusive:

1. **Spot cross-contamination.** Rhynie plant tissue is famously riddled with fungi. A spot on "plant
   cortex" may include fungal material; a spot on a hypha inside a plant cell is mostly plant and
   matrix. This alone could blur the categories, and it is the most likely single explanation.
2. **Optical sampling versus structure thickness.** ATR samples a few micrometres of depth. A hypha a
   micron or two across, embedded in chert, delivers mostly quartz to the spot; a cuticle layer is
   coherent and fills it. Some of what these features measure may be *how much organic matter is in
   the spot*, not what it is made of.
3. **Diagenetic homogenisation** of the nitrogen signal across all tissues after 407 Ma.
4. **Band assignment.** Without table S1 I cannot confirm that band 11 sits at the amide II position;
   the names may not correspond to the bands as strictly as assumed.

---

## What this does and does not show

**It does not show the paper's separation is spurious.** That separation is real and I reproduced it
independently — 0.907 ± 0.097 against a 0.667 baseline for *Prototaxites* vs Fungi
([`data-availability.md`](data-availability.md) §1.2). Something distinguishes these spectra.

**It does show the chemical reading of that separation is unvalidated.** The interpretation —
"fossilization products of sugar-protein compounds," and by extension "*P. taiti* lacked chitin" —
requires the features to track nitrogen. Against tissues whose nitrogen content is known independently,
they do not. And the most chitinous fungal structures in their own dataset score like *Prototaxites* on
the key feature.

**For this repository's own arguments, the effect is corrosive in both directions.** Every quantitative
claim made here from these features — the nitrogen-versus-aliphatic decomposition, the tectin gap
calculation, the amide II differential, the assessment of the aromatic-protein hypothesis — inherits
the same problem. They were all reasoning about nitrogen from features that do not demonstrably measure
nitrogen.

---

## Caveats on this analysis

- **Tissue assignments are mine**, read from Data S2's free-text descriptions. Some are judgement calls
  ("conducting tissues" grouped as lignified, for instance).
- **Small n** for the decisive categories: cuticle 4, hyphae 3, spores 4, amoeba 3.
- The N-free/N-bearing pooling is a coarse dichotomy over materials that differ in much else.
- Every caveat in §3 above applies to the failure as much as to the original interpretation — cross
  contamination could produce this result even if the features were sound.

**The honest summary: the features do not validate as compositional proxies on this dataset, and until
they do, chemical conclusions drawn from them — the paper's and mine alike — are less secure than they
appear.**

---

## Method

Feature values from Data S1 sheet "CCA" (columns as labelled, band numbers 12, 11, 10, 7, 2, 1),
joined to Data S2 specimen descriptions by index; row order verified against the raw spectra sheet
(*Prototaxites* at rows 33–44 in both). Statistics: `scipy.stats.mannwhitneyu`, two-sided.
