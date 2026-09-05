# *Prototaxites* and the fungi share no thin section

Data S2 of Loron et al. lists, for every one of the 102 spectra, the specimen, its England Finder
coordinate and **the slide it came from**. Crossing that with the taxonomic labels answers a question
the paper does not ask.

---

## The contingency table

| slide | Plant | Spore | Fungi | Bacteria | Arthropod | Amoeba | Oomycete | ***Prototaxites*** | total |
|---|---|---|---|---|---|---|---|---|---|
| 2892p | 6 | | 4 | 6 | 3 | | | | 19 |
| Agl2 | 4 | | 12 | | | | | | 16 |
| Agl127 | 1 | 4 | 1 | | 6 | 3 | | | 15 |
| Agl75 2019-1 | 1 | | 4 | | | | 4 | | 9 |
| **G.2024.5.3** | | | | | | | | **7** | **7** |
| Lyon 48 UC1 | 3 | | | | 1 | | | **2** | 6 |
| RFf 2019 | 6 | | | | | | | | 6 |
| G.2024.5.5 | 3 | | | | 2 | | | | 5 |
| **Lyon 156 UCB1** | 1 | | | | | | | **3** | 4 |
| AgLyon 2019 | 3 | | | | | | | | 3 |
| Agl127 2019-2 | 3 | | | | | | | | 3 |
| Rfg | | | 3 | | | | | | 3 |
| NMSRC9 | | | | 3 | | | | | 3 |
| Agl204b, Rfh, Rfe | 2 | | | 1 | | | | | 3 |

*Prototaxites* is on **G.2024.5.3, Lyon 156 UCB1, Lyon 48 UC1**.
Fungi are on **2892p, Agl2, Agl127, Agl75 2019-1, Rfg**.

**The overlap is empty.** Seven of the twelve *Prototaxites* spectra come from G.2024.5.3, a slide
that contributes nothing else at all. Taxon and slide are perfectly aliased for the comparison that
carries the paper's central claim.

The only slides where *Prototaxites* can be compared with anything else in the same section are Lyon
48 UC1 (2 *Prototaxites*, 3 plants, 1 arthropod) and Lyon 156 UCB1 (3 *Prototaxites*, 1 plant). **A
within-section comparison against a fungus is not possible anywhere in the dataset.**

---

## Does slide matter?

Take one taxon and one tissue: plain *Rhynia gwynne-vaughanii* axes — no tracheids, no cuticle, no
decayed axes — **n = 17 across 5 slides**. Any difference between slides here cannot be taxonomy and
cannot be tissue.

| slide | n | aliphatic C–H area, median | range |
|---|---|---|---|
| 2892p | 5 | +0.2805 | +0.1152 to +0.5192 |
| Agl2 | 3 | +0.2643 | +0.1708 to +0.2772 |
| Agl127 2019-2 | 3 | +0.1449 | +0.1341 to +0.1515 |
| AgLyon 2019 | 2 | +0.1378 | +0.1280 to +0.1476 |
| G.2024.5.5 | 3 | +0.0404 | −0.0357 to +0.2457 |

Between-slide range of medians: **0.240**, against a *Prototaxites*–Fungi gap of **0.120**.

On the six published features, within that same one-taxon one-tissue set:

| feature | Kruskal–Wallis p | between-slide range | *Prototaxites*–Fungi gap | |
|---|---|---|---|---|
| N-products | 0.041 | 0.1250 | 0.0766 | slide range exceeds it |
| **Amide II** | **0.030** | **0.1329** | **0.1282** | **slide range exceeds it** |
| N-product + carboxylate | 0.747 | 0.0818 | 0.0856 | |
| Amide I | 0.038 | 0.3595 | 0.2124 | slide range exceeds it |
| CH₂ | 0.188 | 0.3124 | 0.1806 | slide range exceeds it |
| CH₃ | 0.044 | 0.1208 | 0.0464 | slide range exceeds it |

**Said against itself:** these are six tests on 17 spectra. A Bonferroni threshold would be 0.0083 and
none of the p-values clears it. The p-values on their own are suggestive, not conclusive.

The magnitudes do not depend on the p-values, though. For **five of six features, moving between
slides within a single tissue of a single species shifts the feature further than the entire distance
between *Prototaxites* and the fungi.**

---

## The right null

Because taxon and slide are aliased, the honest null is not a random relabelling of specimens — it is
a random regrouping of **slides**. Split the 16 slides into two arbitrary groups of about 12 and 24
spectra, ignore taxonomy entirely, and ask how often that reproduces what is attributed to biology.

| feature | observed gap | null median | null 95th pct | p |
|---|---|---|---|---|
| N-products | 0.0766 | 0.0843 | 0.1860 | 0.535 |
| **Amide II** | 0.1282 | 0.0895 | 0.1858 | **0.300** |
| N-product + carboxylate | 0.0856 | 0.0519 | 0.1177 | 0.216 |
| Amide I | 0.2124 | 0.1095 | 0.2601 | 0.126 |
| CH₂ | 0.1806 | 0.0969 | 0.2472 | 0.166 |
| CH₃ | 0.0464 | 0.0407 | 0.0946 | 0.434 |

**No feature's gap is unusual against slide structure alone.** The Amide II gap — the feature that
most separates *Prototaxites* from Fungi — sits below the null's 95th percentile.

And the headline number itself. Reproducing their classifier on the six published features:

| | accuracy |
|---|---|
| *Prototaxites* vs Fungi | **0.919** (majority baseline 0.667) |
| same classifier, two **arbitrary groups of slides**, taxonomy ignored | median **0.825**, 90th pct 0.897, max 0.992 |
| fraction of slide-splits reaching ≥ 0.919 | **0.043** |

---

## What this does and does not show

**It does not show the result is wrong.** Random groups of slides still contain taxonomic structure —
slides host particular organisms — so the null is not biology-free, and it is inflated in the paper's
favour for that reason. Nor does "slide" isolate one cause: it bundles block provenance and thermal
history, section thickness, mounting, measurement session, and which specimens the operator chose to
target.

**What it does show is structural, and does not depend on any p-value.** With zero slide overlap
between *Prototaxites* and the fungi, no analysis of this dataset can attribute the difference between
them to biology rather than provenance. The two are not separable in principle here.

That matters because provenance is known to vary at Rhynie. Akinsanpe, Bowden & Parnell (2024,
*Palaeogeogr. Palaeoclimatol. Palaeoecol.* 640:112101) measured thermal maturity across Rhynie chert
samples by Raman: **Ro = 0.93 ± 0.10%, range 0.80–1.10% (0.63–1.21% including outliers), n = 20** —
upper oil window, with C29 sterane isomerisation near maximum — and attribute the maturity to
hydrothermal heating that increases toward the basin-bounding fault. Block-to-block maturity varies by
about as much as the whole assemblage's spread. Loron et al. themselves cite Igisu et al.'s (2018,
*Geobiology* 16:412) experiment showing that **aliphatic C–H bonds in silica-embedded cyanobacteria
change under experimental heating** — which is precisely the band on which *Prototaxites* and the
fungi differ.

So the one difference that survived the blank-chert controls in
[`matched-preservation.md`](matched-preservation.md) — *Prototaxites* at half the fungal aliphatic
C–H — is exactly the quantity known to be maturity-sensitive, measured on specimens that never share
a slide with the fungi.

---

## The fix

It is cheap and specific: **measure *Prototaxites* and fungi in the same thin sections.** Rhynie
fungi are abundant and *Prototaxites*-bearing blocks are unlikely to be sterile of them —
[Krings et al. 2018](https://doi.org/10.1098/rstb.2016.0500) review fungi throughout the chert.
A handful of paired within-section measurements would break the aliasing entirely. Failing that,
Raman-derived Ro on each *Prototaxites* and each fungal specimen would let maturity enter as a
covariate.

Until one of those exists, the chemistry cannot carry the weight placed on it — for Loron et al.'s
conclusion, or for any of this project's hypotheses.

## Reproducing

```
cd provenance
python3 slide_confound.py spec_meta.json loron_raw.pkl loron_cca.pkl
```
