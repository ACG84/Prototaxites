# What simulation can contribute

Two were run rather than recommended. One supplied a control I had flagged as the main gap in the
topology work; the other removed an objection to the only hypothesis still standing.

---

## 1. The synthetic tree control — **run, and it validates the measurement**

In [`network-topology-results.md`](network-topology-results.md) §4 I wrote that the result lacked a
matched-noise tree control and that this was "the single thing needed to make the result defensible."
Simulation is exactly the right tool, because you can generate a structure whose topology you know
*by construction* and push it through the identical pipeline.

**Method** (`../network-analysis/synth.py`): build two structure classes as voxel volumes at the same
resolution, tube radius and scale as the fossil —

- **strict tree** — recursive bifurcation with tapering radii. **Zero cycles by construction.**
- **reticulate network** — random nodes wired to k=3 nearest neighbours. **Many cycles by construction.**

Add surface roughness by random boundary erosion/dilation at three levels, then run the same
fill → skeletonise → prune → cycle-basis pipeline. Three seeds each.

### Results

| Structure | Noise | Skeleton length | β₁ (total) | Large circuits | **per unit length** |
|---|---|---|---|---|---|
| strict tree | 0.00 | 44.8 | 107 | 14.7 | **0.33** |
| strict tree | 0.15 | 49.4 | 560 | 33.0 | **0.67** |
| strict tree | 0.30 | 69.9 | 2518 | 74.3 | **1.06** |
| reticulate net | 0.00 | 29.6 | 188 | 84.7 | **2.86** |
| reticulate net | 0.15 | 33.6 | 576 | 113.0 | **3.36** |
| reticulate net | 0.30 | 50.3 | 2001 | 163.3 | **3.25** |
| ***P. taiti* (measured)** | — | **220.2** | — | **1245** | **5.65** |

**Two things are settled.**

**Total β₁ is confirmed worthless.** A structure with *zero* cycles by construction returns β₁ = 107,
560, 2518 as noise rises. That is a pure artifact, and it retrospectively justifies discarding the
β₁ = 744 figure rather than reporting it.

**The large-circuit metric discriminates, and the fossil is far outside the tree range.** Tree:
0.33–1.06 across all noise levels. Reticulate: 2.86–3.36. Non-overlapping, with a clean ~3–5× gap.
*P. taiti* sits at **5.65** — 5–17× the tree control, and about 1.7× the deliberately anastomosing
synthetic network.

So the *P. taiti* medullary spot is not a tree, by a wide margin, and is if anything **more densely
anastomosing than a randomly wired network of the same tube caliber**.

**Limitation.** Synthetic boundary noise is not confocal segmentation noise. This bounds the artifact
rate under a plausible noise model, not the actual one. But at noise = 0.30 the surface is badly
degraded and a tree still only reaches 1.06, so the margin is large.

This does not change the interpretation in `network-topology-results.md` §5 — reticulation remains
taxonomically uninformative, because foraging fungal mycelia are reticulate too. It establishes that
the *measurement* is real, not that it means what we first hoped.

---

## 2. Transport limits on a giant syncytium — **removes an objection to H4**

The surviving hypothesis is that *Prototaxites* was a coenocyte or syncytium rather than a complexly
multicellular organism ([`rhizaria-hypothesis.md`](rhizaria-hypothesis.md) §7). A standing objection is
that a single cell cannot service a metre-scale body. That is calculable.

**Diffusion** (t ≈ L²/2D, D ≈ 10⁻⁹ m²/s for a small metabolite in cytosol):

| Scale | Time |
|---|---|
| *P. taiti* NSC.36, 5.6 cm | 1.6 × 10⁶ s ≈ **18 days** |
| *Syringammina*, 24 cm (a real xenophyophore) | 2.9 × 10⁷ s ≈ **333 days** |
| *P. loganii*, 8 m | 3.2 × 10¹⁰ s ≈ **1,016 years** |

**Bulk streaming** (*Physarum* shuttle streaming ≈ 1 mm/s):

| Scale | Time |
|---|---|
| 24 cm | 240 s |
| **8 m** | 8,000 s ≈ **2.2 hours** |

**Two conclusions.**

Diffusion fails even at *P. taiti*'s 5.6 cm — 18 days to cross. So **any** organism at this scale needs
bulk transport, syncytial or multicellular alike. This does not discriminate grade of organisation, and
should not be offered as though it did.

But bulk streaming at a velocity that real plasmodial protists achieve services **8 metres in about
two hours**. So **transport is not the barrier to a giant syncytium.** The intuition that a single cell
cannot be metres long is wrong on transport grounds, and *Syringammina* already demonstrates the
principle at 24 cm.

The real constraints are elsewhere: nuclear supply (how many nuclei a given cytoplasmic volume
requires), and whether a streaming network can be mechanically maintained through a rigid walled body.
Those are worth modelling and would need parameters this analysis does not have.

Net effect: H4 is modestly strengthened — one objection to it turns out not to hold.

---

## 3. What simulation could contribute next

**Worth doing — forward-modelling into the FTIR feature space.** The live chemical question
([`aromatic-protein-hypothesis.md`](aromatic-protein-hypothesis.md)) is whether a tyrosine-cross-linked
protein can reach *P. taiti*'s coordinates: Amide II 0.017, Amide I 0.30, N-products 0.13, CH₂ 0.25,
CH₃ 0.12. That is a constraint-satisfaction problem. DFT vibrational calculations on model fragments —
a di-tyrosine cross-link, a β-O-4 H-unit lignin dimer, a peptide backbone at increasing degrees of
deamination — would give predicted band intensities to project into the published CCA.

If **no** protein-derived structure at any plausible deamination reaches Amide II = 0.017 while holding
the other five features, the aromatic-protein hypothesis dies computationally, cheaply, before anyone
books a pyrolysis run.

*Caveat that matters:* DFT on fresh molecules is not a diagenetic residue. Modelling the altered
structures means assuming the alteration, which risks assuming the answer. The honest version asks
whether the fossil's coordinates are *reachable*, not what path was taken.

**Not worth doing.**

- **Diagenetic kinetics.** Rate constants for hydrolysis and deamination of heavily cross-linked
  systems are not known. A kinetic model would return its own assumptions. The artificial-maturation
  *experiment* dominates it.
- **Finite-element modelling of the column.** Mechanics depend on wall geometry and material, which a
  syncytium and a multicellular tissue share. It cannot discriminate grade — the question actually at
  issue.

**The general rule this exercise illustrates:** simulation was decisive where it generated a
**control** — a structure with known ground truth run through the same pipeline — and would be weak
where it would have to supply unmeasured parameters. Use it to calibrate methods and bound
possibilities, not to substitute for measurements nobody has taken.

---

## Reproducing

`../network-analysis/synth.py` (structure generators), with `raster.py` and `netlib.py`. Requires
numpy, scipy, scikit-image, networkx.
