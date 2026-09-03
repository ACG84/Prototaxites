# H3′: *Prototaxites* as an allogromiid-grade foraminiferan

The sharpest version of the foraminiferal hypothesis yet proposed, and the one worth stating if the
hypothesis is going to be stated at all. It also fails, but for a more interesting reason than its
predecessors.

---

## 1. Why this is the best version

Every previous formulation carried a character it could not shed. This one sheds most of them.

| Objection that killed earlier versions | Does it apply to an allogromiid? |
|---|---|
| Agglutinated xenophyae absent from *P. taiti* | **No.** Allogromiids build a purely organic test. Nothing to agglutinate, nothing missing. |
| Stercomare absent (40–82% of a xenophyophore) | **No.** Not an allogromiid character. |
| Marine, >500 m only | **No.** Every known non-marine foraminiferan is monothalamid grade — *Edaphoallogromia australica* (tropical forest soil), *Reticulomyxa filosa* (damp soil, decomposing matter), *Haplomyxa saranae* (fresh water). |
| Mineral phase should be visible in Rhynie chert | **No.** No mineral phase to look for. Purely organic preservation is exactly what a soft-walled test would leave. |
| Lineage too young for 407 Ma | **No.** Crown Foraminifera ~770 Ma (650–920). Ample room. |

And the phylogenetic premise is basically right. SSU rRNA and actin phylogenies place monothalamids
at the base of the foraminiferal tree, and the standard reconstruction has the earliest foraminifera
as monothalamous, soft-walled forms resembling extant Allogromiida.

**One taxonomic correction:** Allogromiida is **paraphyletic** — both it and Astrorhizida are grades,
not clades, and molecular work splits "allogromiids" across multiple basal lineages. That does not
damage the argument (a stem lineage is precisely what the hypothesis wants) but it means the group
carries no shared derived characters to reason from. "Allogromiid" here means a grade of organisation:
single-chambered, organic-walled, non-mineralised.

So: this is the version to argue. It is genuinely harder to kill than H1, H2, or the generic H3.

---

## 2. Why it fails anyway

**The non-mineralised character that makes allogromiids attractive is the same character that makes
them chemically worst for the hypothesis.**

Quantitative chemical analysis of the *Allogromia laticollaris* shell:

- **>60% protein**
- **~13% sugars** (galactose and rhamnose)
- trace glucosamine and inorganic components

The suborder Allogromiina is characterised as organic-walled forms built from **proteinaceous
mucopolysaccharide** — "a transparent, flexible shell, consisting partly of acid mucopolysaccharides,
composed of filament-like structural elements embedded in a glue-like substance," predominantly
proteinaceous with acid mucopolysaccharide and lipid.

> **Caveat:** the >60%/13% figures are reported in secondary literature; the primary analysis could not
> be located and verified. The qualitative characterisation (proteinaceous mucopolysaccharide) is
> corroborated independently. Verify the numbers before citing them.

Now recall the discriminator. Loron et al. separate on **sugar–protein alteration products,
"especially the carbonyl and nitrogen moieties."** A test that is >60% protein and ~13% sugar is not
merely compatible with that signal — it is close to a pure specimen of it.

And from the published feature matrix (see [`data-availability.md`](data-availability.md)):

| | Amide II (mean) | Amide I (mean) |
|---|---|---|
| Amoeba (organic protist test, same chert) | 0.1796 | 0.5294 |
| Arthropods | 0.1739 | 0.5148 |
| Fungi | 0.1367 | 0.5478 |
| ***Prototaxites*** | **0.0170** | **0.2771** |

*P. taiti* has the **lowest Amide II of any group in the Rhynie assemblage** — mean 0.0170, median
0.0040. An allogromiid test, being >60% protein, should plot at or beyond the amoeba end of that axis.
It is the single worst candidate in Foraminifera for matching a spectrum with essentially no nitrogen
signal.

**The trade is explicit.** Mineralised foraminifera at least dilute their organic fraction with
carbonate or silica. Choosing the non-mineralised grade removes the mineral objection by making the
organism *entirely* the substance that the chemistry excludes.

---

## 3. The morphological gap is also worst here

Allogromiid tests are **single-chambered sacs** — spherical, oval, sausage-shaped or thread-like, with
one or occasionally two terminal apertures. *P. taiti* is a differentiated system of three tube types
with distinct wall architectures, septa with septal pores in 75% of its volume, annular thickenings in
another, and axial alignment through a coherent cylindrical body.

The deeper mismatch is functional. An allogromiid test is a **container** the cell lives inside. In
*Prototaxites*, the wall **is** the organism — 1–2 µm walls forming 100% of the preserved body, a
structural skeleton rather than an envelope.

**And size runs the wrong way.** Organic-walled allogromiids are typically tens to hundreds of
micrometres (one undescribed species measured 30–60 µm). The one genuinely giant monothalamid,
***Spiculosiphon oceana*** at >4 cm, reaches that size by agglutinating siliceous sponge spicules in
organic cement. That is the pattern across the group: **in monothalamids, size comes with
agglutination.** No organic-walled monothalamid approaches even *P. taiti*'s 5.6 cm, let alone
*P. loganii*'s 8 m — and the one that gets close does it by acquiring exactly the mineral test whose
absence made the allogromiid version attractive.

---

## 4. What this version is worth

It is the correct formulation, and it sharpens the disagreement to a single testable claim.

Earlier versions failed on several independent characters at once — habitat, agglutination, waste
systems, mineral phase. This one collapses all of that into one question:

> **Could a basal, organic-walled foraminiferan have replaced its proteinaceous mucopolysaccharide
> test with a structural polyphenolic wall, and built a metre-scale rigid body out of it?**

Nothing in the fossil record or in extant Foraminifera says yes. But that is now the whole
disagreement, and it is a cleaner question than anything the hypothesis had before.

---

## 5. The experiment this makes possible

This version is more tractable than the Devonian-lining route in
[`control-experiment.md`](control-experiment.md), for a simple reason: **the material is culturable.**

*Allogromia laticollaris* is a long-established laboratory organism. Other organic-walled monothalamids
are collectable from intertidal and shelf sediments (Gooday 2002 surveys occurrence and ecology). So:

1. Culture or collect organic-walled monothalamid tests; isolate them.
2. **Artificially mature** them to a maturity calibrated on the Rhynie fossils (Raman, or their
   published band ratios: CH₃/CH₂ ≈ 0.71–0.75, ~C9 chains). This is the step that makes the comparison
   taphonomically legitimate, and it is non-optional.
3. Compute the six band intensities Loron et al. use — `N-products`, `Amide II`,
   `N-product+carboxylate`, `Amide I`, `CH2`, `CH3` — per their table S1 definitions.
4. Project into the published CCA using their released pipeline and matrix.

Step 3 is the reason this is now cheap: **only six numbers are needed**, not archived raw spectra.

**Prediction, stated in advance:** a matured allogromiid test will plot at or beyond the amoeba
position on the nitrogen axes, far from *P. taiti*. If it instead plots near *Prototaxites*, the
chemical argument against every foraminiferal hypothesis collapses at once — and that would be the
most interesting possible outcome, so the experiment is worth running either way.

---

## 6. Verdict

**H3′ (allogromiid grade) is the strongest form of the hypothesis and still fails.** It is upgraded
from its predecessors in structure — it sheds the agglutination, stercomare, habitat and mineral-phase
objections cleanly — but it concentrates all the remaining weight on wall chemistry, where the
evidence is now quantitative and points the wrong way: >60% protein against the lowest Amide II
signature in the Rhynie assemblage. Morphology and size add independent problems, and the one
monothalamid that achieves *Prototaxites*-adjacent size does so by agglutinating.

The [§7 grade-of-organisation argument](rhizaria-hypothesis.md) remains untouched and remains the part
of this whole line of enquiry most likely to be right.

---

## References

- Pawlowski J, Holzmann M, Tyszka J (2013). New supraordinal classification of Foraminifera: molecules
  meet morphology. *Mar. Micropaleontol.* [paraphyly of Allogromiida and Astrorhizida]
- Pawlowski J et al. (2003). The evolution of early Foraminifera. *PNAS*.
  https://www.pnas.org/doi/10.1073/pnas.2035132100
- Gooday AJ (2002). Organic-walled allogromiids: aspects of their occurrence, diversity and ecology in
  marine habitats. *J. Foraminiferal Res.*
- Holzmann M, Pawlowski J (2021). Review: freshwater and soil Foraminifera. *J. Foraminiferal Res.* 51:318.
- Maldonado M et al. (2013). *Spiculosiphon oceana* sp. nov. (Foraminifera, Astrorhizida), a giant
  foraminifer converging on the feeding strategy of carnivorous sponges. *Zootaxa* 3669:571–584.
  https://mapress.com/zootaxa/2013/f/zt03669p584.pdf
- Tyszka J, Godos K, Goleń J, Radmacher W (2021). *Earth-Sci. Rev.* 220:103726.
- Loron CC et al. (2026). *Sci. Adv.* 12(4):eaec6277; feature matrix at
  https://github.com/nrodgers1/Prototaxites-Analysis-code
