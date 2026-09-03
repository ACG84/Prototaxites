# Where this stands

A synthesis after working through the Xenophyophorea → Foraminifera → Allogromiida sequence, the
chemical evidence, and the network topology. Written because the position has moved several times and
some of those moves were corrections to my own errors.

---

## 1. The nematophyte suggestion was circular — withdrawn

I proposed at the end of the classifier reproduction that the live alternative to "new lineage" was a
**nematophyte** affinity, on the grounds that *Prototaxites* sits nearest plants in the FTIR space and
*Nematoplexus* plotted with plants in the 2023 data.

That was a bad suggestion, for a reason that should have been obvious:

- **Nematophyta is explicitly a wastebasket taxon.** The group lacks a clear definition, is
  paraphyletic, and was erected by Lang (1937) precisely as a holding category for Silurian–Devonian
  tube-built organisms that were "neither algae nor vascular plants."
- ***Prototaxites* is already in it.** It sits in Nematophytaceae alongside *Nematoplexus* and
  *Nematasketum*. *Nematophyton* is a synonym of *Prototaxites*.

So "*Prototaxites* is a nematophyte" restates the problem in older vocabulary. It is not an answer, and
grouping it chemically with another nematophyte establishes nothing about affinity — only that
tube-built Silurian–Devonian organisms share a wall chemistry, which is what put them in the same
wastebasket in the first place.

---

## 2. The chemistry constrains what it *isn't* far better than what it *is*

The reproduction in [`data-availability.md`](data-availability.md) §1.2 splits cleanly into two
inferences of very different quality.

**The negative inference is robust.** *P. taiti* lacks the sugar–protein recondensation products that
the 24 co-occurring Rhynie fungi retain through identical silicification. Classification against Fungi
reproduces at 0.907 ± 0.097 versus a 0.667 baseline. Whatever the wall was, it was not a glycoprotein
or mucopolysaccharide.

This is not confounded by ecology: an organism with a glycoprotein wall would show those products
whatever it was doing for a living. And it is the inference that damages H3′ hardest, since an
allogromiid test is **>60% protein**.

**The positive placement is not robust.** *Prototaxites* barely separates from plants — 0.800 versus a
0.755 baseline, a margin of 0.045, with single features exactly at baseline.

And there is a straightforward explanation that involves no phylogenetic signal at all: **a polyphenolic
structural wall is what you need to build a rigid, self-supporting body on land.** Land plants converged
on lignin for that reason. If *Prototaxites* independently evolved a polyphenolic wall for the same
mechanical reason, its position near plants in this space tracks **"built a rigid terrestrial body,"**
not **"is related to plants."**

If that is right, the FTIR fingerprint is partly a **functional** signal, and its taxonomic resolution
is asymmetric: good for excluding wall chemistries an organism did not have, poor for placing it.

That is a caution against Loron et al.'s positive claim as much as against any alternative — including
the one I suggested.

---

## 3. Every line so far is exclusionary

| Line | What it establishes | What it places |
|---|---|---|
| FTIR wall chemistry | Not glycoprotein/chitinous → not fungal, **not rhizarian** | Nothing (positive side confounded, §2) |
| Perylene absence | Not ascomycete | Nothing |
| No photobionts | Not lichen | Nothing |
| Banded tubes | No fungal parallel | Nothing — orphan character |
| Network topology | Densely reticulate, ~1,245 large circuits | Nothing — convergent across fungi, myxomycetes, algae, rhizarians |
| No xenophyae, no stercomare, deep-marine-only habitat | Not Xenophyophorea | Nothing |
| >60% protein allogromiid test | Not allogromiid | Nothing |

Everything constrains; nothing places. Loron et al.'s "previously undescribed lineage" is the residue
of that elimination — which is exactly why the elimination's completeness matters so much.

---

## 4. The one argument that has survived everything

From [`rhizaria-hypothesis.md`](rhizaria-hypothesis.md) §7, unchanged through every round:

Loron et al. reach "new lineage" by exhausting the three supergroups that contain **complexly
multicellular** organisms. Nothing in the paper establishes that *Prototaxites* was complexly
multicellular. Xenophyophores demonstrate that a decimetre-scale, structurally differentiated tubular
body can be built by a single cell.

Note that this argument does not require *Prototaxites* to be a rhizarian — and given §2, it had better
not, because the chemistry excludes the rhizarian wall. It requires only that the **grade of
organisation is undetermined**, which no evidence gathered here has settled.

The character that bears on it most directly remains unexamined: **septal pore ultrastructure** in the
Type 1 tubes carrying 75% of body volume. A perforate septum is not a cell boundary. "Septate with
pores" reads more naturally as a compartmentalised coenocyte than as multicellular tissue, and pore
geometry would discriminate.

---

## 5. Honest status of the original hypothesis

| | Status |
|---|---|
| **H1** Xenophyophorea | Falsified — multiple diagnostic characters absent |
| **H2** Stem-xenophyophore | Vacuous — strips every defining character |
| **H3** Foraminifera broadly | Substantially weakened — glycoprotein wall chemistry |
| **H3′** Allogromiid grade | Best-formulated and still fails — >60% protein is the worst possible match to the lowest Amide II in the assemblage |
| **H4** Giant syncytium, unspecified affinity | **Live and untested** |

The sequence was worth running. It moved from a specific identification that fails on many characters,
to a sharper one that fails on one well-measured character, to a grade-level claim that nothing yet
addresses. That is the right direction of travel for a hypothesis even when the answer keeps coming
back negative.

---

## 6. Corrections made along the way

Recorded because several affected conclusions:

1. **Chitin in foraminiferal linings** — stated as established; it is disputed, and Tyszka et al. say
   composition "was never elucidated in detail." Withdrawn; replaced by the nitrogen argument, which
   does not depend on it.
2. **"No living analogue for a foram changing wall chemistry"** — wrong. Silicoloculinida secrete
   opaline silica; composite calcite+opal tests exist. Corrected, with the observation that the
   lability runs uniformly toward biomineralisation, never toward structural organic aromatics.
3. **"Allen et al. 2000 is print-only"** — wrong. Freely hosted by the Grzybowski Foundation.
4. **β₁ = 744 loops in Mask_7** — a voxelisation artifact. Vertex-cloud grids are not watertight below
   ~0.005 model units; the value ranged 74–24,260 across parameters. Replaced with triangle
   rasterisation and a resolution-stable large-circuit metric.
5. **"The topology result undercuts Loron et al."** — overstated. Their anti-fungal case rests
   primarily on the chemistry, which is independent and stronger.
6. **"The live alternative is nematophyte"** — circular, §1 above.
