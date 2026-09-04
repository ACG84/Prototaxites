# What structure would explain a missing amide I?

First a correction to the previous document, then the structural answer.

---

## 1. Correction: "no amide I" was too strong

[`raw-spectra-analysis.md`](raw-spectra-analysis.md) reported the absence as a "discrete, qualitative
presence/absence." Applying Loron et al.'s own second-derivative method (Savitzky-Golay, order 2,
window 21) shows that is **overstated**.

**Group means** — local second-derivative minima in 1560–1720 cm⁻¹:

| Group | Amide I component | All local minima (cm⁻¹, d² ×10³) |
|---|---|---|
| Amoeba | **yes** | 1566 (1.62), 1610 (−7.26), **1650 (0.62)**, 1689 (−3.19) |
| Fungi | **yes** | 1566 (2.06), 1612 (−6.69), **1653 (0.66)**, 1687 (−2.43) |
| Arthropod | **yes** | 1566 (1.67), 1612 (−7.30), **1653 (0.80)**, 1689 (−3.14) |
| Plant | no | 1612 (−7.43), 1687 (−3.12) |
| Bacteria | no | 1610 (−7.54), 1685 (−2.99) |
| ***Prototaxites*** | no | **1573 (2.81)**, 1612 (−8.51), 1687 (−3.71) |

**Per spectrum**, the difference is a tendency rather than a dichotomy:

| Group | spectra with a 1638–1668 cm⁻¹ component |
|---|---|
| Amoeba | 2/3 (67%) |
| Arthropod | 8/12 (67%) |
| Fungi | 15/24 (62%) |
| Bacteria | 6/10 (60%) |
| Plant | 16/33 (48%) |
| ***Prototaxites*** | **4/12 (33%)** |

Two things follow. **Individual *Prototaxites* spectra do sometimes show an amide I component** — a
third of them. And the 1650 feature is a **weak shoulder** in every group: the local minima there are
*positive* in the second derivative (0.62–0.80 ×10⁻³), whereas a strong band gives a negative minimum
like the 1612 feature at −6.7 to −8.5.

So the accurate statement is: **amide I is weak-to-absent in *Prototaxites*, weaker than in the
proteinaceous groups, and this is a quantitative tendency rather than a categorical absence.** That is
weaker than I claimed and it loosens the constraint on what structure is required.

One genuinely *Prototaxites*-specific feature does emerge: a component at **1573 cm⁻¹** present in no
other group's mean. Aromatic ring stretch, carboxylate asymmetric stretch, or conjugated C=C are the
candidates.

---

## 2. Structures that would produce this signature

The constraint set, assembled from all sources:

- strong aromatic C=C (1612, the dominant band)
- phenolic — oxygen-substituted aromatic (¹³C NMR shoulder at 155 ppm; alkylphenols on pyrolysis)
- conjugated carbonyl (1687), and carboxyl (1710)
- ether linkages
- aliphatic present but **low** (*Prototaxites* is aliphatic-poor)
- **no polysaccharide ensemble** (1200–800 cm⁻¹)
- amide I weak-to-absent; very low nitrogen overall (Abbott: C, H, O)
- pyrolysis gives alkylbenzenes, alkylphenols, **naphthalene and alkylnaphthalenes**, biphenyl, PAHs

### The candidates

**(a) Generic N-free polyphenolic network** — the paper's reading. Aromatic, phenolic, ether-linked,
some carbonyl, no nitrogen. Fits everything. Its weakness is that it is a description rather than a
structure: "extinct polyphenolic biomacromolecule" names the gap rather than filling it.

**(b) DHN-melanin — the most specific candidate, and it has not been considered**

This is worth separating out, because **Loron et al. treat "melanin" as one category and it is two
chemically distinct polymers**:

| | Precursor | Nitrogen | Backbone |
|---|---|---|---|
| **DOPA / eumelanin** | tyrosine | **contains N** (indole) | indolequinone |
| **DHN-melanin** | polyketide (1,8-dihydroxynaphthalene) | **nitrogen-free** | naphthalenoid |

DHN-melanin is the characteristic **fungal** melanin, and it is a polyketide with **no nitrogen at
all**. It would give: strong aromatic C=C, phenolic O-substituted aromatic, quinone carbonyl, extreme
diagenetic resistance, no polysaccharide — and **no amide I, with no diagenetic special pleading
required.**

And it matches Abbott's pyrolysate in a specific way: DHN-melanin depolymerises to **naphthalenes and
phenols**, and Abbott found naphthalene "prominent" with C1-alkylnaphthalenes and alkylphenols
abundant.

This also explains my dinocyst measurement. The eumelanin standard I analysed
([`dinocyst-data-analysis.md`](dinocyst-data-analysis.md)) peaks at 1570 cm⁻¹ with strong 1620–1510
absorption — because it is the **nitrogen-containing** melanin. DHN-melanin would not show those
features. The two melanins are not interchangeable and the literature discussion has been conflating
them.

**(c) Condensed tannin / proanthocyanidin-like polyphenol** — N-free, aromatic, phenolic, resistant,
pyrolyses to phenols. Plausible; less specific than (b).

**(d) Sporopollenin-like polyketide-phenolic** — phenolic + alkane + ketone + lactone + carboxylic
acid, which is close to the observed band list. The objection is that *Prototaxites* is aliphatic-poor
and sporopollenin is not, plus the embryophyte-specific biosynthesis.

**(e) A protein that lost its backbone** — the aromatic-protein hypothesis, now requiring peptide
hydrolysis with survival of a cross-linked aromatic side-chain network. Weakened further by §1 only in
the sense that the constraint is looser; the differential-diagenesis problem is unchanged.

---

## 3. Two caveats that cut against the melanin route

**Perylene.** Loron et al. searched for perylene — derived from **perylenequinones**, fungal pigments —
and found it **absent in *P. taiti*, present in the substrate**. That is direct evidence against
fungal pigment chemistry in the fossil, and it constrains (b).

**Naphthalene is maturity-confounded.** Naphthalene, phenanthrene and anthracene are classic thermal
maturation PAHs. At Abbott's Ro 0.77–1.03% they form from almost any organic precursor. So the
naphthalene match to DHN-melanin is suggestive, not diagnostic. Testing it needs the **Rhynie chert**
material, which is thermally immature — and pyrolysis has never been run on that.

---

## 4. What this means for the hypothesis

Every structure that comfortably explains the signature is a **nitrogen-free polymer**: polyphenolic
network, DHN-melanin, condensed tannin, sporopollenin-like polyketide. None is a protein.

The protein route is not excluded — the constraint is softer than §1 originally claimed, and a third of
*Prototaxites* spectra do carry an amide I component — but it remains the only candidate that needs
diagenesis to remove something that was there, while the others explain the observation by the polymer
never having had a peptide backbone.

**And note where (b) points.** If the wall were DHN-melanin, that is a *fungal* biosynthetic product,
and the reading becomes "a heavily melanised organism whose chitin was lost while its melanin survived"
— a known taphonomic pattern, since melanised fungal structures preserve preferentially. That
possibility argues against Loron et al.'s conclusion in a different direction from the rhizarian
hypothesis, and their own perylene result is the main evidence against it.

The discriminating experiment is unchanged and now more pointed: **pyrolysis on the thermally immature
Rhynie chert material**, looking for naphthalenediol and naphthalenone products (DHN-melanin) versus
N-heterocycles (protein) versus methoxyphenols (lignin). Three structural hypotheses, three distinct
product suites, one unrun experiment.

---

## Method note

Second derivative computed with `scipy.signal.savgol_filter(window_length=21, polyorder=2, deriv=2)`
on the D1 processed spectra (1450–2999 cm⁻¹), matching the parameters Loron et al. state. Local minima
found with `argrelmin(order=2)`.
