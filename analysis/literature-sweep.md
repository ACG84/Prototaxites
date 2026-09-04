# Deeper literature sweep: two corrections and what was actually found

A broader search turned up work I had missed, and it overturns two claims made in this repository —
one of them repeated across several documents.

---

## Correction 1: pyrolysis **has** been run on *Prototaxites*

[`aromatic-protein-hypothesis.md`](aromatic-protein-hypothesis.md) §5 is headed "The decisive test has
never been run," and I stated in several places that pyrolysis GC-MS had never been applied to
*Prototaxites*. **That is wrong.**

> **Abbott GD, Ewbank G, Edwards D, Wang GY (1998). "Molecular characterization of some enigmatic
> Lower Devonian fossils." *Geochimica et Cosmochimica Acta* 62:1407–1418.**
> doi:10.1016/S0016-7037(98)00078-7

They analysed coalified *Prototaxites*, *Pachytheca* and *Parka* by **three** techniques:

- **flash pyrolysis-GC-MS**
- **FTIR**
- **¹³C solid-state NMR**

Result: the flash pyrolysates of well-preserved *Prototaxites* and *Pachytheca* were **"dominated by
aromatic hydrocarbons and alkylphenols."**

What was true is narrower: **Loron et al. (2026) ran no pyrolysis.** The technique was applied to the
organism 27 years earlier, on coalified material from a different taphonomic setting.

### What this does to the aromatic-protein hypothesis

It weakens it, but does not settle it, and the reason matters.

**Alkylphenols are precisely the ambiguous class.** Allen et al. (2000) flagged it from the other
direction: phenols and methylphenols "may not be specific for tyrosine since these products may also
originate from a non-proteinaceous phenolic biopolymer." So a pyrolysate dominated by aromatic
hydrocarbons and alkylphenols is compatible with either a polyphenol or a tyrosine-rich protein.

**What would break the tie is the N-heterocycles** — indole, pyrrole, nitriles, diketopiperazines — and
no summary I can access mentions any. But **I have not read the full paper** (paywalled, and Cardiff's
repository record returned 403), so I cannot say they were absent from the data rather than absent from
the abstract. 1998 GC-MS sensitivity for trace nitrogen compounds is also lower than modern practice.

**¹³C solid-state NMR is the more surprising omission from my earlier reasoning.** It distinguishes
amide carbonyl from aromatic and aliphatic carbon directly, and it was run in 1998. Anyone pursuing
this should read that paper before proposing new analyses.

---

## Correction 2: the H-type monomer dominance is **not** from *Prototaxites*

[`aromatic-protein-hypothesis.md`](aromatic-protein-hypothesis.md) §2 builds the tyrosine argument on
the claim that "Abbott et al.'s alkaline oxidation of *Prototaxites* yielded lignin monomers dominated
by H-type." **That attribution appears to be wrong.**

The H-dominance result comes with the qualifier "**preserved by rapid silicification**," which points
to the Rhynie chert, not to Abbott's coalified siltstone and sandstone material. It traces to:

> **Holman AI, Poropat SF, Greenwood PF, Bhandari R, Tripp M, Hopper P, Schimmelmann A, Brosnan L,
> Rickard WDA, Wolkenstein K, Grice K (2024). "Significance of lignin and fungal markers in the
> Devonian (407 Ma) Rhynie Chert." *Geobiology* 22(4):e12616.**

Their methods: hydropyrolysis (HyPy) of kerogen, alkaline oxidation for lignin monomers, and
high-resolution mass-spectrometric mapping of a thin section. Findings: H-dominated monomer
distribution with G and S subordinate; perylene concentrated in kerogen and **localised within
silicified plant fragments**, linking it to phytopathogenic fungi.

**That is a bulk Rhynie chert sample, not *Prototaxites*.** The chert contains abundant land plants,
which are the obvious lignin source.

So the tyrosine argument's central empirical hook — "the anomalous H-dominance is exactly what a
tyrosine-rich protein would give" — **does not currently attach to *Prototaxites***. It is an
observation about Rhynie chert bulk organic matter.

The chemical point stands in principle: tyrosine is p-hydroxyphenylalanine and would yield H-type
oxidation products. But it is no longer supported by a measurement on the fossil in question, and
§2 of that document overstates its evidential basis. **The hypothesis is weaker than I presented it.**

---

## What the sweep confirms rather than overturns

**Nitrogen remains unmeasured, and the field knows it.** From Abbott's own 2014 doctoral project
description:

> "Previous work has shown that mid-Palaeozoic plant fossils are composed of **carbon, hydrogen and
> oxygen**"... "Novel techniques are beginning to extend the analytical window including **further
> elements such as nitrogen**."

The proposed programme included XPS, ToF-SIMS, helium ion microscopy, TMAH depolymerisation with ¹³C
labelling — explicitly "**to help distinguish lignin from other polyphenols**" — and "carbon and
nitrogen measurements."

Two things follow. The working characterisation of these fossils is **C/H/O**, consistent with low
nitrogen but not itself a measurement. And **Abbott independently identified the same ambiguity** this
repository arrived at: distinguishing lignin from other polyphenols is the open problem, and TMAH with
isotope labelling is his proposed tool for it.

**XPS deserves flagging** — it gives elemental composition *and* chemical state, including the N 1s
region. It would answer the nitrogen question directly and appears not to have been applied to
*Prototaxites*.

---

## Other items located

- **Cooper LM, Loron CC, Hetherington AJ (2025). "*Prototaxites*." *Current Biology*** — a primer by
  the same group, published between the preprint and the *Science Advances* paper.
- **Boyce CK, Cody GD, Fogel ML, Hazen RM, Alexander CMO'D, Knoll AH (2003). "Chemical evidence for
  cell wall lignification and the evolution of tracheids in early Devonian plants." *Int. J. Plant
  Sci.* 164:691–702** — carbon XANES on Devonian material; cited by Loron et al. Whether *Prototaxites*
  was included is worth checking, since XANES is another compositional technique not otherwise
  considered here.
- **"Mineralization controls informative biomarker preservation"**, *Geobiology* (gbi.70030) and
  **"Molecular and mineral biomarker record of terrestrialization in the Rhynie Chert"** — further
  Rhynie organic geochemistry, unread.

---

## Net effect

The sweep **cost the aromatic-protein hypothesis its main empirical support** (Correction 2) and
**removed the claim that its decisive test was unavailable** (Correction 1) — the test was run, and
returned aromatic hydrocarbons and alkylphenols, which is the ambiguous answer rather than a
supportive one.

It also showed that the analytical gap this repository has been circling is one the specialists
identified independently and proposed to close a decade ago: **distinguish lignin from other
polyphenols, and measure the nitrogen.** Whether that work was ever completed is the next thing to
check.

---

## References

- Abbott GD, Ewbank G, Edwards D, Wang GY (1998). *Geochim. Cosmochim. Acta* 62:1407–1418.
  https://www.sciencedirect.com/science/article/abs/pii/S0016703798000787
- Holman AI et al. (2024). *Geobiology* 22(4):e12616. https://onlinelibrary.wiley.com/doi/10.1111/gbi.12616
- Cooper LM, Loron CC, Hetherington AJ (2025). *Prototaxites*. *Current Biology*.
  https://www.cell.com/current-biology/abstract/S0960-9822(25)01675-6
- Boyce CK et al. (2003). *Int. J. Plant Sci.* 164:691–702.
- Abbott GD (2014). IAPETUS project IAP/14/35, "Molecular characterization of mid-Palaeozoic plant
  fossils." https://iapetus.ac.uk/wp-content/uploads/2014/11/IAP_14_35-NEW-Abbott.pdf
- Allen K, Roberts S, Murray JW (2000). Grzybowski Found. Spec. Publ. 7, 1–13.
