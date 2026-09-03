# Network topology of the *P. taiti* medullary spot: first quantitative results

The 3D data is public and I analysed it. Headline: **the traced tube systems are pervasively
reticulate, not tree-like** — but the result is worth less to this hypothesis than it first appears,
and one of my intermediate numbers was an artifact that I nearly reported.

---

## 1. The data

Edinburgh DataShare **doi:10.7488/ds/7895** (CC-BY). The landing page is JavaScript-rendered and blocks
naive fetching, but the DSpace REST API serves files directly — see
[`../network-analysis/README.md`](../network-analysis/README.md).

The deposit contains:

| File | Size | What |
|---|---|---|
| `MPEG0057 spot model .obj` | 248 MB | **3D model of a medullary spot** — the branching network |
| `MPEG0057_..._airyscan_Substack (1-114)_zstack.tif` | 1.48 GB | Raw Airyscan confocal z-stack, 114 slices |
| `NSC 36 cut_scaled.obj`, `NSC36 whole block_scaled.obj`, `block 156 scaled.obj` | 1.2 GB | Photogrammetry of chert blocks (external) |
| `Images_of_sampled_fossils.zip` | 1.9 GB | Microphotographs |

The spot model derives from thin section **NMS G.2024.5.7 (MPEG0057)**. It contains **2,158,666
vertices, 4,324,760 triangles, in 24 separately segmented masks** — each mask a traced tube system.

---

## 2. A false result, and how it was caught

First pass: voxelise the vertex point cloud, fill, skeletonise, count independent loops (cyclomatic
number β₁). Mask_7 gave **β₁ = 744**, and it was completely invariant to spur pruning — which looked
like strong evidence the loops were real.

It was an artifact. A resolution sensitivity sweep gave:

| voxel | closing=0 | closing=1 | closing=2 |
|---|---|---|---|
| 0.006 | 458 | 95 | 74 |
| 0.004 | 3578 | 353 | 164 |
| 0.003 | 24260 | 2718 | **744** |
| 0.002 | (mesh leaked) | 23661 | 8851 |

β₁ ranged over **two orders of magnitude** depending on arbitrary parameters. The cause: median
triangle edge length is 0.0031 model units, so a vertex-only voxel grid is not watertight below ~0.005.
Fine grids leak (spurious loops through holes); coarse grids plus closing weld adjacent tubes together
(spurious fusions).

**Any single number from that pipeline is meaningless.** I nearly reported 744 as a finding.

---

## 3. The corrected pipeline, and what survives

Fix: rasterise the **triangles** by barycentric supersampling, giving a watertight shell at any
resolution. Total β₁ is *still* resolution-dependent (392 → 488 → 789 → 893 → 1274 from voxel 0.006 to
0.0025), because skeletonising a noisy segmented solid keeps generating small surface loops.

So absolute loop counts remain unmeasurable. But **loop size** separates signal from noise: segmentation
noise makes loops on the scale of surface roughness, real anastomoses make loops on the scale of tube
spacing. Measuring the physical cycle-size spectrum:

| voxel | β₁ (unstable) | circuits > 0.05 | **> 0.20** | mean tube radius |
|---|---|---|---|---|
| 0.005 | 488 | 205 | 114 | 0.0116 |
| 0.004 | 789 | 320 | **170** | 0.0103 |
| 0.003 | 893 | 353 | **169** | 0.0094 |

**Large circuits converge**: 170 and 169 at the two finest resolutions. A circuit of perimeter 0.20 is
roughly **20× the mean tube radius** — far too large to be surface roughness.

### Across all 24 masks (voxel 0.004)

Large circuit = perimeter > 20× that mask's mean tube radius.

- **Total skeleton length: 220.2 units**
- **Large circuits: 1,245** — density **5.65 per unit skeleton length**
- **Degree-3 junctions: 9,404**; **degree ≥ 4: 1,106**
- Per-mask large-circuit density: **4–7 per unit** in every substantial mask (Mask_1 4.2, Mask_6 7.3,
  Mask_7 5.6, Mask_16 6.8, Mask_20 6.2, Mask_21 5.9, Mask_24 4.2)
- Mean tube radius is consistent across masks: **0.0085–0.0106 units** — one caliber class

Reticulation is a **general property of every traced tube system**, not a feature of one mask.

**A branching tree has zero closed circuits at any scale.** These have thousands.

---

## 4. What this does not establish

**No matched-noise control.** I have no tree-like mesh put through the same confocal segmentation and
the same pipeline. Without it, "not a tree" is strongly indicated but not proven — large loops from
noise are implausible at 20× tube radius, but implausible is not excluded. **This is the single thing
needed to make the result defensible**, and it is easy: process a synthetic branching tree with matched
surface roughness, or a confocal stack of a known tree-like structure, identically.

**Scale is uncertain.** The OBJ carries no physical calibration, so everything above is in model units
and tube radii. Absolute tube diameters cannot be checked against the paper's 10/20–40/40 µm classes
without the z-stack metadata.

**Fragmentation.** Each mask breaks into multiple connected components on voxelisation (Mask_7: 112 at
voxel 0.004); only the largest was analysed. Whether that fragmentation is real or a segmentation
artifact is unresolved.

---

## 5. Why this matters less to the hypothesis than expected

Here the honest conclusion runs against my own earlier framing, which called this "the best test
available."

**Reticulate, non-hierarchical filament networks are not a rhizarian character.** Cord-forming and
foraging fungal mycelia — *Phanerochaete*, *Armillaria* and relatives — build extensively anastomosing
networks with high loop density. Hyphal fusion is a normal, well-documented fungal behaviour. So a
network with thousands of closed circuits and ~9,400 three-way junctions is **entirely compatible with
Fungi**.

That has two consequences:

1. **It weakens Loron et al.'s argument, not the fungal hypothesis.** They used medullary-spot
   branching — "three dimensional and highly complex," with "no discernible branching hierarchy" — as
   a structural argument against Fungi. Foraging mycelial networks look like this. The character does
   not do the work they ask of it.
2. **It gives the rhizarian hypothesis nothing.** The observation that originally motivated this whole
   line — non-hierarchical anastomosis as a granuloreticulosan signature — is convergent across fungi,
   myxomycetes, algae and rhizarians. Confirming it quantitatively confirms something taxonomically
   uninformative.

This is what makes network architecture a **poor phylogenetic character but a useful similarity
search**. It cannot establish affinity. Once affinity is constrained by other evidence, quantitative
comparison against candidate analogues could narrow *which* analogue — that is a legitimate second-stage
use, not a first-stage test.

---

## 6. What would make it useful

The numbers above are one side of a comparison with nothing on the other side. To be worth anything they
need identically-processed comparators:

| Comparator | Availability |
|---|---|
| Xenophyophore granellare | Gooday et al. 2018 micro-CT, *Sci. Rep.* (PMC6092355) — 3D data published |
| Fungal mycelial network | Extensive published network datasets; **the critical one**, given §5 |
| *Physarum* plasmodium | Well characterised; non-fungal, non-rhizarian control |
| Foraminiferal reticulopodia | Light microscopy mostly; 3D is scarce |
| **Synthetic tree, matched noise** | Must be generated — the control from §4 |

Until at least the fungal comparator and the tree control are run through this same pipeline, the
correct statement is: *the P. taiti medullary spot is a densely reticulate network with ~5.7 large
circuits per unit skeleton length, and that is compatible with several unrelated groups.*

---

## 7. Reproducing

Code in [`../network-analysis/`](../network-analysis/): `raster.py` (watertight voxelisation),
`netlib.py` (skeleton graph, pruning, cyclomatic number, junction angles). Requires numpy, scipy,
scikit-image, networkx. Download instructions in that directory's README.
