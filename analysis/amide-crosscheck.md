# Cross-checking amide I against tissues of known composition

Data S2 gives per-specimen taxon **and tissue type** for all 102 spectra, so the assemblage can be
broken into materials whose original composition is known. Doing that tests whether the 1650 cm⁻¹
component behaves like a protein marker at all.

**It does not.** This result weakens my own reasoning of the previous two documents, and it bears on
the paper's interpretation as well.

---

## The test

Amide I component = local minimum in the second derivative between 1638–1668 cm⁻¹ (Savitzky-Golay,
order 2, window 21 — their stated parameters), on the D1 processed spectra.

| Tissue category | n | with amide I | mean 1650 height |
|---|---|---|---|
| **PLANT cuticle** — cutin, an **N-free polyester** | 4 | **2/4** | 0.4255 |
| PLANT tracheid / conducting — lignified | 7 | 4/7 | 0.4391 |
| **PLANT decayed axis** — visibly degraded | 1 | **1/1** | **0.6423** ← highest of all |
| PLANT axis / cortex — parenchyma, protein-rich in life | 19 | 8/19 | 0.4063 |
| **FUNGUS glomeromycotan spores** — thick-walled, chitinous | 4 | **1/4** | 0.3961 |
| FUNGUS hyphae | 3 | 2/3 | 0.4344 |
| FUNGUS *Palaeomyces* | 16 | 11/16 | 0.6127 |
| ***PROTOTAXITES* body tubes** | 7 | **0/7** | 0.2642 |
| ***PROTOTAXITES* medullary spots** | 5 | **4/5** | 0.3175 |

---

## Three things this shows

### 1. The 1650 component appears in a nitrogen-free polymer

**Plant cuticle is cutin** — a polyester of hydroxy fatty acids, containing no nitrogen. Two of four
cuticle spectra carry a 1638–1668 cm⁻¹ component, at a mean height (0.4255) well above *Prototaxites*.

A band that appears in cutin is not diagnosing protein. Ester C=O, conjugated carbonyl and aromatic
C=C all absorb in this region, and in thermally altered fossil organic matter they overlap the amide
position.

### 2. Degradation does not remove it — the decayed specimen has the most

The one specimen the authors label **"decayed axis"** has the **highest 1650 height in the entire
assemblage (0.6423)** and a clear amide I component.

This is the direct answer to the question the crosscheck was designed to ask. If protein degradation
erased amide I, the visibly degraded specimen should be the one lacking it. It is the opposite.

### 3. Chitinous spores often lack it

**Glomeromycotan spores are chitinous and protein-bearing by any account, and only 1/4 show the
component** — the same rate as *Prototaxites* body tubes, and worse than plant cuticle.

So presence does not track protein and absence does not track its lack.

---

## What the *Prototaxites* split actually shows

The sharpest contrast in the table is internal:

| | amide I | h(1650) range |
|---|---|---|
| **Body tubes** (7) | **0/7** | 0.190–0.331 |
| **Medullary spots** (5) | **4/5** | 0.283–0.332 |

Body tubes uniquely lack the component — the only category in the assemblage at 0. Medullary spots
mostly have it. The 1650 *heights* overlap between the two, so this is about whether a separate
component resolves, not about intensity.

That contrast is anatomical, not compositional in any obvious way, and it sits awkwardly against Loron
et al.'s synchrotron result that spots and body are chemically similar (CH₃/CH₂ 0.71 vs 0.75). Two
readings: the spots contain denser or different organic material — plausibly cytoplasmic residue rather
than wall — or the spots' greater optical density simply resolves components the thinner tube walls do
not.

Either way, **the body tube walls — the material the whole affinity argument is about — are the one
category in the Rhynie assemblage with no resolvable 1650 component at all.**

---

## Consequences

**For my previous two documents.** [`raw-spectra-analysis.md`](raw-spectra-analysis.md) and
[`what-structure.md`](what-structure.md) treated the amide I absence as evidence about protein content,
and built a structural argument on it. That inference does not hold: in this material the 1650
component appears in N-free cutin, peaks in a decayed axis, and is scarce in chitinous spores. **The
"no amide I therefore no protein backbone" reasoning is withdrawn.**

What survives is narrower and still real: *Prototaxites* body tubes are the only category with **no**
resolvable component, and they sit lowest on mean height. That is a genuine outlier position. It is
just not interpretable as "no protein" without a band assignment that this cross-check shows is
unsafe.

**For the paper.** Amide I (band 7) and Amide II (band 11) are two of the six features driving their
CCA, and the axis is interpreted as "fossilization products of sugar-protein." If the 1650 region is
not protein-specific in this material — appearing in cutin, absent in chitinous spores — that
interpretation carries less weight than presented. The **separation** they report is real and I
reproduced it (0.907 vs 0.667 baseline); what the separating features *mean* chemically is less
settled.

**Caveats on my own test.** My 1638–1668 window is a choice, not theirs — table S1 would give the
actual position of band 7. The second-derivative local-minimum criterion is a crude detector, and small
categories (cuticle n = 4, spores n = 4, decayed axis n = 1) carry wide uncertainty. The decayed-axis
result in particular is a single specimen and should not be leaned on alone.

---

## What this makes worth doing

The cross-check design is sound and should be extended rather than abandoned. With table S1's band
positions, the same tissue-level breakdown could be run on all six features at once, asking: **which
features track original composition, and which track thermal or optical artefacts?** The Rhynie
assemblage is unusually well suited to it because it contains cutin, lignin, chitin, cellulose and
protein-rich tissues in one diagenetic setting.

That is a stronger use of this dataset than anything attempted here, and it would tell you how much of
the *Prototaxites* result is chemistry.

---

## Method

Specimen categories assigned from Data S2 tissue descriptions, joined to Data S1 spectra by ID number.
Second derivative via `scipy.signal.savgol_filter(21, 2, deriv=2)`; components located with
`argrelmin(order=2)`.
