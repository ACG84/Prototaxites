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

## Standing question

Loron et al. reach "previously undescribed lineage" by elimination across the three supergroups that
contain complexly multicellular organisms. The paper never establishes that *Prototaxites* **was**
complexly multicellular. Xenophyophores show that a decimetre-scale differentiated tubular body can
be built by a single cell. That is the thread these notes pull on.
