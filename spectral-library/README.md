# Reference spectral library

## What is here

`kimmel_parse.py` — extractor for the **Kimmel Center Infrared Spectral Library** (Prof. Steven
Weiner, Weizmann Institute): *"FTIR spectra of natural and biogenic materials, as occurring in
archaeological sciences."* **363 spectra, 208–4000 cm⁻¹, ~1.93 cm⁻¹ step.**

`kimmel_parsed.pkl` — the parsed result, `{name: (wavenumbers, absorbance)}`.

Download the source archive from
`https://www.effemm2.de/spectragryph/databases/Kimmel_Center_IR_spectra_library_363entries.zip`
(free, 3 MB), unzip, and run the parser on the `.sgdr` file. Original library:
http://www.weizmann.ac.il/kimmel-arch/infrared-spectra-library

## Why this library

It happens to contain nearly every endmember this project needs, plus something rarer.

**Biopolymers**
- **Chitin** — two preparations (crab shell Sigma; β-form purified squid pen)
- **Cellulose**, **Lignin**, **Starch**
- **Keratin** (fingernail; peacock feather quill), **Silk** (*Bombyx mori*; spider), **Wool**
- **Collagen — fresh *and* fossil**: pure fresh, cornea, fossil bone insoluble fraction ×2,
  and one **>50,000 BP**

**Diagenetic series** — the reason this library is unusually valuable here
- Collagen: fresh → fossil → >50,000 BP
- Wood: fresh pine / tamarisk → fossil wood ×2 → fossil bark
- Charcoal: fresh wood → fossil (Kebara Cave)
- Bone: fresh goat → burnt series (Burn = 0…6) → fossil ×4
- **Humic acids** ×4 — degraded organic matter endmembers

**Matrix minerals**
- **Flint** (a chert — the direct Rhynie matrix analogue), **Quartz**
- **Opal-A**, **Opal-CT**, "opal transforming", **Diatomite**, **phytoliths** (biogenic silica)

## Validation

Extraction was checked against known band positions:

| Material | Recovered peaks (cm⁻¹) | Expected |
|---|---|---|
| Quartz | 1066, 1153, **781/762**, 496, 444 | Si–O asym ~1080, doublet ~798/779 |
| Flint | 1070, **781/762**, 677, 445 | as quartz — confirms chert |
| Cellulose | 1041, 1095, 1147, 1014 | polysaccharide C–O |
| Chitin | **1641 (amide I), 1539 (amide II)**, 1097, 1055 | textbook |
| Collagen, fresh | **1633, 1531, 1223** | amide I / II / III |
| **Collagen, >50,000 BP** | **1631, 1523, 1221** | — |
| Keratin | 1637, 1523 | amide I / II |

## The result that matters immediately

**Fossil collagen older than 50,000 years still shows amide I at 1631 and amide II at 1523**, at
essentially the same positions as fresh collagen (1633 / 1531).

That is a direct empirical datum on the question this project has circled repeatedly: **protein amide
bands are not readily lost on burial.** It does not settle the Rhynie case — 50 kyr is not 407 Myr,
and burial in cave sediment is not silicification — but it removes "amide bands just degrade away" as
a free assumption.

## What this enables

1. **Matrix correction.** Flint and quartz endmembers allow the chert contribution to be modelled and
   removed from the Rhynie spectra. This is the most defensible use, because minerals do not alter the
   way biopolymers do — and it directly addresses the ATR-sampling-depth confound raised in
   [`../analysis/feature-validation.md`](../analysis/feature-validation.md).
2. **Testing the features.** The six Loron features can be computed on chitin, cellulose, lignin,
   collagen and keratin directly, to see whether "Amide II" actually separates them.
3. **A diagenetic axis.** Fresh→fossil pairs give an empirical handle on which bands survive burial.

## The caveat that does not go away

These are **modern or Quaternary** references. Fitting them to a 407 Ma silicified fossil is the same
taphonomic mismatch this project has flagged throughout. Endmember fitting can say *what the fossil
spectrum resembles*; it cannot say what the organism was made of without maturation-matched
references, which no library contains.

Mineral endmembers are the exception and can be used directly.
