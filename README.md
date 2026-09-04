# Prototaxites

Working notes testing alternative phylogenetic hypotheses for *Prototaxites* against the data in
Loron et al. (2026), *Science Advances* 12(4):eaec6277 — "*Prototaxites* fossils are structurally and
chemically distinct from extinct and extant Fungi."

## Contents

- [`analysis/rhizaria-hypothesis.md`](analysis/rhizaria-hypothesis.md) — Does a Xenophyophorea, or
  more broadly Foraminifera, affinity fit the *Prototaxites taiti* data? Character-by-character
  assessment, the falsifiers, four diagnostic tests that would settle it, and the one part of the
  argument that survives.
- [`analysis/control-experiment.md`](analysis/control-experiment.md) — Can a rhizarian be run through
  Loron et al.'s classifier? What a taphonomically valid control requires, the one that already exists
  in their published dataset, the Devonian foraminiferal linings that could serve as a direct test,
  and the thermal-maturity trap that would produce a false positive.
- [`analysis/foram-wall-chemistry.md`](analysis/foram-wall-chemistry.md) — Do foraminifera actually
  require a glycoprotein wall? Withdraws the chitin argument, tests whether any foraminiferan lacking
  glycoprotein structures could serve as an analogue, and finds the ones that do lack it are
  mineralised.
- [`analysis/allogromiid-hypothesis.md`](analysis/allogromiid-hypothesis.md) — H3′: the
  allogromiid-grade version, which sheds the agglutination, stercomare, habitat and mineral-phase
  objections and is the strongest form of the hypothesis. Fails because the non-mineralised character
  that makes it attractive is what makes it >60% protein.
- [`analysis/data-availability.md`](analysis/data-availability.md) — Audit of what data already
  exists. The 2026 feature matrix and pipeline are public; the amoeba control is recomputed from them
  (and is n = 3); the key foraminiferal FTIR study exists in print only; xenophyophore wall chemistry
  is genuinely uncollected.

- [`analysis/other-evidence.md`](analysis/other-evidence.md) — Eleven independent lines beyond FTIR
  chemistry, ordered by how much can be done with data that already exists. Top three: network topology
  from the public 3D reconstructions, bulk C/N, and a sulfate band that may already be sitting
  unexamined in acquired spectra.

- [`analysis/network-topology-results.md`](analysis/network-topology-results.md) — First quantitative
  analysis of the public 3D medullary-spot model. The network is pervasively reticulate (~1,245 large
  circuits, 9,404 three-way junctions), but an earlier intermediate result was a voxelisation artifact,
  and the finding turns out to be taxonomically uninformative because foraging fungal mycelia are
  reticulate too. Code in [`network-analysis/`](network-analysis/).

- [`analysis/aromatic-protein-hypothesis.md`](analysis/aromatic-protein-hypothesis.md) — Could a
  tyrosine-rich cross-linked structural protein, rather than a polyphenol, explain the "lignin-like"
  signature? It would explain the anomalous H-type monomer dominance, it would materially help H3′, and
  the technique that settles it — pyrolysis GC-MS — has never been applied to *Prototaxites*.
- [`analysis/tectin-variants.md`](analysis/tectin-variants.md) — Could a different tectin composition
  explain the readings? Documented variation doesn't close the gap, but the protist test matches
  *P. taiti* on aliphatics almost exactly (0.25 SD) and differs almost purely on nitrogen — and Amide II
  falls twice as hard as Amide I, which is the signature of N–H modification rather than protein
  absence.
- [`analysis/existing-analogues.md`](analysis/existing-analogues.md) — Hunting a positive analogue.
  Nothing in Rhizaria, but dinosporin has four distinct spectrochemical groups, some sporopollenin-like
  and one melanin-bearing — refuting "a protist can't evolve a plant-like resistant wall." Nitrogen,
  however, is present in all of them.
- [`analysis/deep-sea-monothalamid-chemistry.md`](analysis/deep-sea-monothalamid-chemistry.md) — Does
  any exist? No. Confirmed by search: mineralogy, ultrastructure and phylogeny only. The nearest taxon
  is *Astrammina rara* (Antarctic, shallow), whose cross-linking turns out to be disulfide rather than
  di-tyrosine.
- [`analysis/abbott-1998-read.md`](analysis/abbott-1998-read.md) — Having read Abbott 1998, Holman
  2024 and the Loron main text: the 1998 pyrolysis was run at Ro 0.77–1.03% where it cannot
  discriminate, so its lack of nitrogen products is uninformative; the H-type lignin result is
  definitively not about *Prototaxites*; and Loron et al. state that melanin-type material "would be
  hidden by the stronger general kerogen signal" — a declared blind spot covering the aromatic-protein
  hypothesis.
- [`analysis/raw-spectra-analysis.md`](analysis/raw-spectra-analysis.md) — **The raw 102-spectrum
  dataset.** *Prototaxites* resolves no amide I peak at 1650 cm⁻¹, while the amoeba, fungi and
  arthropods each do. A discrete qualitative difference, and the hardest evidence yet against an
  aromatic-protein wall.
- [`analysis/what-structure.md`](analysis/what-structure.md) — What structure explains a missing
  amide I? Softens the previous claim (it is a tendency, not an absence), then works through the
  candidates. Raises DHN-melanin — the nitrogen-free polyketide fungal melanin, chemically distinct
  from the tyrosine-derived eumelanin everyone has been discussing.
- [`analysis/dinocyst-data-analysis.md`](analysis/dinocyst-data-analysis.md) — The 219-spectrum
  dinocyst dataset, analysed. Its eumelanin standard peaks at 1570 cm⁻¹ — a tyrosine-derived aromatic
  polymer absorbs strongly exactly where *P. taiti* is weakest.
- [`analysis/literature-sweep.md`](analysis/literature-sweep.md) — Deeper sweep. Two corrections:
  pyrolysis GC-MS, FTIR and ¹³C NMR were all run on *Prototaxites* by Abbott et al. in 1998, and the
  H-type lignin monomer dominance describes bulk Rhynie chert (Holman et al. 2024), not the fossil.
  Both weaken the aromatic-protein hypothesis.
- [`analysis/wanted-papers.md`](analysis/wanted-papers.md) — Ranked list of papers to obtain, with
  what each would settle.
- [`analysis/simulation.md`](analysis/simulation.md) — Two simulations run, not recommended. A
  synthetic tree control validates the topology measurement (trees yield 0.33–1.06 large circuits per
  unit, reticulate networks 2.86–3.36, *P. taiti* 5.65) and confirms total β₁ is an artifact. A
  transport calculation shows bulk streaming services 8 m in ~2 hours, removing an objection to the
  syncytium hypothesis.
- [`analysis/where-this-stands.md`](analysis/where-this-stands.md) — Synthesis. Why every line of
  evidence so far is exclusionary rather than placing, why the chemistry's positive side may be a
  functional signal rather than a phylogenetic one, the status of each hypothesis, and a list of the
  corrections made along the way.

## Standing question

Loron et al. reach "previously undescribed lineage" by elimination across the three supergroups that
contain complexly multicellular organisms. The paper never establishes that *Prototaxites* **was**
complexly multicellular. Xenophyophores show that a decimetre-scale differentiated tubular body can
be built by a single cell. That is the thread these notes pull on.
