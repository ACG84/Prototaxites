# Specimen provenance

`spec_meta.json` — `{id: {desc, slide}}` for all 102 spectra, parsed from Data S2 of Loron et al.
(2026). Data S2 is a single free-text column in which several specimens often share a line, and two
slide names contain digits (`Lyon 48 UC1`, `Lyon 156 UCB1`) that a naive parse reads as specimen
numbers; `parse_s2()` in `slide_confound.py` handles both. All 102 ids resolve to one of 16 slides.

`slide_confound.py` — crosses provenance with the taxonomic labels. The finding is that **no slide
contains both a *Prototaxites* spectrum and a fungal one**, so taxon and slide are perfectly aliased
for the paper's central comparison. The script quantifies what that costs: the slide effect within a
single taxon and tissue, and a slide-permutation null for both the feature gaps and the classifier
accuracy.

Results and caveats in [`../analysis/slide-confound.md`](../analysis/slide-confound.md).

Needs `loron_raw.pkl` and `loron_cca.pkl`, parsed from the Data S1 `Raw spectra` and `CCA` sheets.
