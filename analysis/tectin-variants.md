# Could a different tectin composition produce the *P. taiti* readings?

"Tectin" is a placeholder term — Hedley criticised it as chemically undefined in 1963 and Tyszka et al.
(2021) still say foraminiferal wall composition "was never elucidated in detail." So the claim that an
allogromiid wall *must* be glycoproteinaceous rests on a handful of measured taxa, not on a constraint
established across the group. That is a fair place to push.

Quantifying it produces the most interesting result in this line of work so far, and it points somewhere
slightly unexpected.

---

## 1. What tectin is actually known to vary in

| Taxon | Composition | Source |
|---|---|---|
| *Allogromia laticollaris* | >60% protein, ~13% galactose + rhamnose, trace glucosamine | secondary lit. |
| *Astrammina rara* | Glycoproteinaceous, collagen-like; amide I at **1635 cm⁻¹** (β-sheet) | Allen et al. 2000 |
| *Jadammina macrescens*, *Trochammina inflata* | Glycoproteinaceous; amide I at **1652 cm⁻¹** (α-helix) | Allen et al. 2000 |
| *Gromia* | Predominantly proteinaceous + acid mucopolysaccharide + **lipid**; multilayered honeycomb membranes | — |
| General | Sulfated glycosaminoglycans; S=O detectable at 1250–1230 cm⁻¹ | Hedley 1963; Langer 1992 |

So there is **real documented variation** — in protein:sugar ratio, in secondary structure (β-sheet vs
α-helix between taxa), in sulfation, and in lipid content.

And wall *type* is strikingly labile: **"the transformation from organic to agglutinated wall occurred
several times in monothalamous lineages,"** many lineages contain both organic and agglutinated
species, and **"some may even change the nature of their test wall depending on the environmental
conditions."**

**But note where the lability runs.** It runs organic ↔ agglutinated — i.e. whether mineral grains are
added. There is no documented monothalamid that swapped protein–mucopolysaccharide for a *different
organic chemistry*. Every tectin anyone has measured is protein plus polysaccharide.

---

## 2. Quantifying the gap: what a variant would have to change

Using the published feature matrix, distance from the *Prototaxites* centroid decomposed into the
nitrogen features (N-products, Amide II, N-product+carboxylate, Amide I) and the aliphatic features
(CH₂, CH₃), scaled by each feature's pooled SD:

| Group | N-space distance | Aliphatic distance | **Ratio N : aliphatic** |
|---|---|---|---|
| **Amoeba** | 2.82 | **0.25** | **11.42** |
| Arthropods | 2.67 | 0.71 | 3.76 |
| Fungi | 2.42 | 0.73 | 3.33 |
| Plant | 1.64 | 0.83 | 1.97 |
| Bacteria | 1.13 | 3.07 | 0.37 |

**This is the striking result.** On the aliphatic features, the protist organic test is the **closest
match to *P. taiti* in the entire dataset** — 0.25 SD, against 0.73 for fungi and 0.83 for plants. The
separation between a protist test and *Prototaxites* is almost **purely nitrogenous**, and by a much
larger margin than for any other group.

Put plainly: strip the nitrogen from the amoeba and it lands on *Prototaxites*.

What a tectin variant would have to do to make that trip:

| Feature | Amoeba | *P. taiti* | Change | In pooled SD |
|---|---|---|---|---|
| **Amide II** | 0.1796 | 0.0170 | **−91%** | −1.54 |
| N-prod + carboxylate | 0.2536 | 0.1272 | −50% | −1.49 |
| N-products | 0.2564 | 0.1333 | −48% | −1.02 |
| **Amide I** | 0.5294 | 0.2771 | **−48%** | −1.53 |
| CH₂ | 0.2316 | 0.2493 | +8% | +0.08 |
| CH₃ | 0.0942 | 0.1179 | +25% | +0.23 |

Lose roughly half the nitrogen signal, ~90% of Amide II specifically, and change essentially nothing
else.

---

## 3. The pattern of nitrogen loss is not what protein *absence* looks like

Amide I is roughly 80% C=O stretch. Amide II is roughly 60% **N–H in-plane bend** plus C–N stretch. The
two bands therefore respond differently to different causes:

- **Removing protein** should drop Amide I and Amide II together, roughly in proportion.
- **Modifying N–H** — substitution at nitrogen, cross-linking involving the amide N, or strong hydrogen
  bonding — suppresses **Amide II preferentially** while Amide I persists.

Observed: **Amide II −91%, Amide I −48%.** Nearly a twofold differential, in the direction that
indicates N–H modification rather than protein removal.

That is a quantitative argument for the cross-linked-protein reading
([`aromatic-protein-hypothesis.md`](aromatic-protein-hypothesis.md)) that does not depend on any
parsimony intuition. It says the fossil retains a protein-like carbonyl signature while having lost its
N–H character — which is what a heavily tanned or cross-linked protein should look like, and not what a
polyphenol that never had amides should look like.

### Caveats, and they are substantial

- **Amide II at 0.0170 is near zero.** Percentage changes against a near-zero denominator are unstable,
  and baseline-fitting artifacts dominate at that end of the scale.
- **I do not have their table S1 band definitions**, so I do not know the exact integration limits, and
  band overlap in the 1600–1500 cm⁻¹ region is severe in fossil organic matter.
- **n = 3 for the amoeba.** This is a centroid comparison on a very small group.
- Alternative explanation: Amide II is generally the more diagenetically labile of the two bands
  independent of any cross-linking, so preferential loss may just be maturity.

This is a hypothesis-generating observation, not a result. It should be checked against the raw spectra
at doi:10.7488/ds/3806 with explicit band definitions before anyone leans on it.

---

## 4. Verdict

**A different tectin composition does not close the gap on its own.** The documented variation — in
protein:sugar ratio, secondary structure, sulfation, lipid content — is variation *within* a
protein-plus-polysaccharide design, and none of it approaches a 50–91% nitrogen reduction. The
compositional lability that *is* documented in monothalamids runs organic ↔ agglutinated, which is the
wrong axis: it adds mineral grains, and *P. taiti* has none.

**But the shape of the discrepancy is informative, and it favours modification over composition.** The
protist test already matches *P. taiti* on aliphatics almost exactly (0.25 SD). The entire disagreement
is one axis, and the way the loss is distributed across that axis — Amide II falling twice as hard as
Amide I — points to nitrogen being *altered* rather than *never present*.

So the productive question is not "which tectin composition?" but "**what happens to a tectin that is
heavily cross-linked at nitrogen?**" That has an experimental answer: quinone-tan or peroxidase-crosslink
a modern allogromiid or *Gromia* test, artificially mature it, and measure the Amide II/Amide I ratio.
If cross-linking drives that ratio toward the fossil's while leaving aliphatics alone, the hypothesis
has real support. If it does not, the polyphenol reading stands.

That experiment is cheaper than everything else outstanding in this repository, and it tests the one
axis on which the whole disagreement now rests.

---

## References

- Tyszka J et al. (2021). *Earth-Sci. Rev.* 220:103726 — "never elucidated in detail."
- Allen K, Roberts S, Murray JW (2000). Grzybowski Found. Spec. Publ. 7, 1–13 — β-sheet vs α-helix
  variation, sulfated GAG band. https://gf.tmsoc.org/Documents/IWAF-5/Allen+Roberts+Murray-IWAF5-1997.pdf
- Hedley RH (1963); Langer MR (1992) — sulfated GAGs.
- Loron CC et al. (2026), *Sci. Adv.* 12(4):eaec6277 — feature matrix via
  https://github.com/nrodgers1/Prototaxites-Analysis-code
- Loron CC et al. (2023), *Nat. Commun.* 14:1387 — raw spectra doi:10.7488/ds/3806
