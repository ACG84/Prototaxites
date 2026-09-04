# Endmember fitting of the Rhynie spectra — and why it does not work

The proposal was straightforward: take a unified library of biomaterial FTIR spectra, fit the Rhynie
spectra as non-negative mixtures of reference endmembers, and read off composition. The library was
found and extracted ([`../spectral-library/`](../spectral-library/)). The fit was run. It fails — and
the way it fails is more informative than a success would have been.

## Method

Endmembers: 24 spectra from the Kimmel Center library — mineral matrix (quartz, flint, calcite,
kaolinite), modern biopolymers (chitin, cellulose, lignin, starch, collagen, keratin, pine wood,
terpenoid resin), Quaternary organics (humic acid, charcoal, buried wood, collagen >50 ka, copal), and
the deep-time maturation series (Miocene / Eocene / Cretaceous amber, Jurassic jet, Carboniferous coal,
anthracite, bitumen).

Targets: group-mean spectra of the 102 Rhynie spectra from Loron et al. Data S1 — eight groups, six of
which have known or uncontroversial composition.

Fit: non-negative least squares on baseline-corrected, vector-normalised spectra. Preprocessing was
not chosen by eye. `sweep.py` runs 28 combinations of derivative order, smoothing width and spectral
window, and scores each by an **internal control**: the rank the correct endmember receives for
tissues whose composition is known — chitin for arthropod cuticle and fungi, lignin/cellulose/wood for
plant axes, protein for cyanobacteria.

## The control result

| Preprocessing | Arthropod → chitin | Fungi → chitin | Plant → lignin/cellulose | Bacteria → protein | mean R² |
|---|---|---|---|---|---|
| 2nd deriv, w=13, 1350–1800 + 2800–3050 | 12 / 24 | 15 / 24 | 11 / 24 | 11 / 24 | 0.26 |
| 2nd deriv, w=31, 1500–1800 | 6 / 24 | 6 / 24 | 2 / 24 | 9 / 24 | 0.56 |
| 1st deriv, w=31, 1200–1800 + 2800–3050 | 14 / 24 | 6 / 24 | 2 / 24 | 9 / 24 | 0.74 |
| **rubberband, 1500–1800** | **6 / 24** | **6 / 24** | **1 / 24** | 9 / 24 | 0.63 |
| **rubberband, 1200–1800 + 2800–3050** | 5 / 24 | 5 / 24 | 6 / 24 | 9 / 24 | **0.85** |

(rank of the correct endmember by fitted weight, out of 24; 1 is best)

Across every variant tried:

* **Plant tissue recovers lignin** — often rank 1. Lignocellulose survives 407 Ma recognisably.
* **Chitinous tissue never recovers chitin better than rank 5 or 6 of 24**, in any variant.
* **Protein-rich cyanobacteria never recover a protein endmember better than rank 9 of 24**, in any
  variant.

## What the fits actually return

Best-R² variant (rubberband, 1200–1800 + 2800–3050):

| Rhynie group | known composition | fitted mixture | R² |
|---|---|---|---|
| Plant | lignocellulose | 43% kaolinite, 27% flint, 26% anthracite | 0.86 |
| Arthropod | chitin + protein | 46% kaolinite, 28% anthracite, 24% flint | 0.88 |
| Fungi | chitin | 44% kaolinite, 26% anthracite, 26% flint | 0.89 |
| Bacteria | protein-rich | 46% kaolinite, 26% anthracite, 8% Cretaceous amber | 0.86 |
| Amoeba | proteinaceous test | 48% kaolinite, 29% flint, 24% anthracite | 0.87 |
| ***Prototaxites*** | **unknown** | **46% kaolinite, 28% anthracite, 18% flint** | 0.75 |

Restricting to 1500–1800 to force the fit onto the organic region:

| Rhynie group | fitted mixture | R² |
|---|---|---|
| Plant | 46% lignin, 45% kaolinite, 9% coal | 0.62 |
| Arthropod | 41% kaolinite, 39% lignin, 12% coal | 0.69 |
| Fungi | 52% kaolinite, 40% lignin | 0.76 |
| Bacteria | 49% kaolinite, 44% lignin | 0.67 |
| Amoeba | 41% lignin, 41% kaolinite, 18% coal | 0.70 |
| ***Prototaxites*** | **50% lignin, 42% kaolinite, 8% copal** | 0.42 |

**Every group returns the same answer.** A chitin-and-protein arthropod cuticle, a chitinous fungal
hypha, a proteinaceous amoeba test and a lignified plant axis are indistinguishable under this method.
The mixture weights carry no group-discriminating information at all.

## Two consequences

**1. The "lignin-like signature" of *Prototaxites* is not a *Prototaxites* result.** In the organic
window, lignin takes 39–50% of the fit for *cyanobacteria* and for *amoeba tests* as readily as for
*Prototaxites*. Nothing in the Rhynie assemblage can be distinguished from lignin by spectral
matching. The earlier question — whether a tryptophan-rich protein could produce a lignin-like
signature ([`tectin-variants.md`](tectin-variants.md)) — does not need answering, because the
lignin-likeness is generic to this material rather than specific to *Prototaxites*.

**2. Absence of a chitin match is not evidence of absence of chitin.** Fungal hyphae in the Rhynie
chert are chitinous, and they do not match modern chitin either. Whatever the FTIR of this assemblage
records, it is not recoverable composition by reference matching.

The reason is visible directly in the maturation series ([`../spectral-library/README.md`](../spectral-library/README.md)):
Jurassic jet — coalified conifer wood, nitrogen-free, composition known — sits at 1604, 1441, 1373,
1255 cm⁻¹, Carboniferous coal at 1601, 1443, 1375, 1259, and anthracite retains a single band at
1583. Every Rhynie group is dominated by a band at 1612–1614. That band is where thermal alteration
puts aromatic C=C. It is a maturation feature, and it is the same in all of them.

## What this does and does not touch

It does **not** refute Loron et al. Their SVM is trained on Rhynie fossils and tested on Rhynie
fossils; it never appeals to a modern reference spectrum, so it is not vulnerable to the mismatch
demonstrated here. The internal weakness of their classification is a separate matter, established in
[`feature-validation.md`](feature-validation.md) from their own feature values.

It does close off the approach proposed here. Endmember fitting against a reference library cannot
determine what *Prototaxites* was made of, and the demonstration is that it cannot determine what the
arthropods were made of either — and we know.

## What would be needed

A reference set that is **maturation-matched**: biological tissues of known composition, taken to
Ro ≈ 0.8% and silicified, then run under the same ATR conditions. No library contains one. Confined
hydrous-pyrolysis experiments on chitin, tectin, cellulose and protein, run to Rhynie-equivalent
maturity, would produce it. That is a laboratory programme, not a data-mining exercise — which is the
same conclusion reached from the other direction in [`control-experiment.md`](control-experiment.md).

## Reproducing

```
cd spectral-library
python3 kimmel_parse.py Kimmel_Center_IR_spectra_library_363entries.sgdr kimmel_parsed.pkl
python3 fit.py kimmel_parsed.pkl loron_raw.pkl      # loron_raw.pkl built from Data S1
python3 sweep.py                                    # the control sweep
```
