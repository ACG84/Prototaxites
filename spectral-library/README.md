# Reference spectral library

## What is here

`kimmel_parse.py` — extractor for Spectragryph `.sgdr` databases (binary format reverse-engineered).
Tested on two:

| Database | entries parsed | content |
|---|---|---|
| **Kimmel Center Infrared Spectral Library** (S. Weiner, Weizmann) | 363 / 363 | natural and biogenic materials, archaeological sciences |
| **RRUFF FTIR** | 882 / 882 | minerals only — no organics beyond graphite and whewellite |

`kimmel_parsed.pkl` — parsed Kimmel library, `{name: (wavenumbers_ascending, absorbance)}`.
`fit.py` — non-negative-least-squares endmember fitting of the Loron et al. Rhynie spectra.
`sweep.py` — preprocessing sweep, scored by whether tissues of known composition recover their own endmember.

Sources (both free):
`https://www.effemm2.de/spectragryph/databases/` →
`Kimmel_Center_IR_spectra_library_363entries.zip`, `RRUFF_FTIR_DB_882entries_01.zip`.
Original Kimmel library: http://www.weizmann.ac.il/kimmel-arch/infrared-spectra-library

---

## Correction to the first version of this file

The first parser assumed the record header sat at fixed float indices 28/29. That was wrong twice:

* **94 of the 363 records** have the header at a different offset and were silently given a nonsense
  wavenumber axis (spans of ~1e-179). Among them were four of the five ambers, both coals, all the
  fresh and fossil wood, and two fossil bones — i.e. most of the deep-time entries.
* The remaining 269 were **shifted nine points (~17 cm⁻¹) low**.

`kimmel_parse.py` now locates the header by its signature — six consecutive `-1.0` sentinels followed
by a plausible (X_end, −step) pair — and all 363 records parse with a sane axis. Band positions below
are the corrected ones and now match the literature to within 1–3 cm⁻¹. **The numbers in the previous
version of this table were all ~17 cm⁻¹ too low.**

The conclusion drawn from them is unchanged, and marginally strengthened: fossil collagen older than
50,000 BP shows amide I at **1651** and amide II at **1545**, against **1647 / 1545** for fresh
collagen — no measurable shift.

---

## Validation

| Material | Recovered (cm⁻¹) | Literature |
|---|---|---|
| Quartz | 1084, 798, 779, 513, 461 | 1085, 798, 779, 512, 460 |
| Flint (chert) | 1088, 798, 781, 509, 463 | as quartz |
| Calcite | 1423, 876, 712 | 1420, 875, 712 |
| Cellulose | 1373, 1338, 1165, 1115, 1059, 1032 | polysaccharide C–O |
| Lignin | 1605, 1513, 1459, 1208, 1042 | aromatic C=C 1600/1510 |
| Chitin (α, crab) | **1658 (am I), 1556 (am II)**, 1377, 1115, 1072, 1030 | 1660, 1556 |
| Chitin (β, squid pen) | **1651**, 1431, 1381, 1153, 1074, 1038 | β-chitin amide I unsplit |
| Collagen, fresh | **1647, 1545**, 1452, 1336, 1240 | 1650, 1550, 1240 |
| **Collagen, >50,000 BP** | **1651, 1545**, 1452, 1336, 1240, 1082 | — |
| Keratin (fingernail) | **1653, 1541**, 1454, 1398, 1240 | 1650, 1540 |

---

## The deep-time entries — answer to "are there older samples?"

No curated FTIR library contains pre-Quaternary *biological tissue*. But the Kimmel library, filed
under archaeological raw materials, contains a **thermal-maturation series of plant-derived organic
matter running back to the Carboniferous**:

| Entry | Material | Age | Diagnostic bands recovered |
|---|---|---|---|
| Wood (Pine fresh) | lignocellulose | modern | 1510, 1425, 1375, 1267, 1063 |
| Humic Acid (Huleh peat) | humified OM | Holocene | 1618, 1419, 1034 |
| Copal (Philippines) | immature resin | sub-fossil | 1695, 1645, 1468, 1448, 1232, 1176 |
| Amber (Dominican Rep.; Chiapas) | resin | Miocene ~15–20 Ma | — |
| **Amber (Baltic)** | resin | **Eocene ~34–48 Ma** | 1716, 1456, 1381, 1236, 1163, 1026 |
| Amber (Hermon, Israel) | resin | Cretaceous (Levantine belt) | — |
| **Amber (New Jersey)** | resin, Raritan Fm | **Late Cretaceous ~90 Ma** | 1701, 1452, 1379, 1230, 1161, 1028 |
| **Jet (England)** | **coalified conifer wood** | **Early Jurassic ~182 Ma** (Whitby) | 1604, 1441, 1373, 1255, 814, 752; 2918/2854 |
| **Coal** | humic coal | Carboniferous | 1601, 1443, 1375, 1259, 814; 2920/2862 |
| **Anthracite (Ward's)** | coal, high rank | maturation endpoint | **1583 only** |
| Bitumen (Iraq; Oman), Asphalt (Dead Sea, Hasbeya, Nahal Hemar) | migrated hydrocarbon | geological | — |

Plus a shallower series that is still useful: fossil wood ×2 (Cave of Letters), fossil bark (Gesher
Benot Ya'aqov, ~780 ka), fossil charcoal (Kebara), fossil bone collagen ×4, fossil date, phytoliths.

**Jet is the single most useful entry in the library for this project.** Its original composition is
known and uncontroversial — conifer lignocellulose, nitrogen-free — and it has been through
coalification. It is the only reference here that is both a *tissue of known composition* and
*thermally matured*.

### What still does not exist anywhere

**A thermally matured biological tissue of known original composition, other than wood.** There is no
matured chitin, no matured protein, no matured polysaccharide reference in any library checked
(Kimmel, RRUFF, IRUG, OpenSpecy, EPA, SDBS, NIST, U. Minnesota archaeological materials). The one
Mendeley dataset that looked promising — *"The organic matter type in the shale rock samples assessed
by FTIR-ATR analyses"*, 22 Carpathian Flysch shales with Rock-Eval and vitrinite reflectance — turns
out to contain **only the article PDF**, no spectra.

The two genuinely maturation-matched datasets this project holds are therefore both already in hand:
**Loron et al.'s own 102 Rhynie spectra** (407 Ma, one chert, one preparation, tissues of known
composition) and **Abbott et al. 1998's coalified *Prototaxites* material** (Ro 0.77–1.03%).

---

## What the maturation series shows

The Rhynie spectra are dominated by a band at 1612–1614 cm⁻¹ in **every** group — plant, fungus,
arthropod, cyanobacterium, amoeba and *Prototaxites* alike ([`../analysis/raw-spectra-analysis.md`](../analysis/raw-spectra-analysis.md)).

Jet at 1604, coal at 1601 and anthracite at 1583 place that band exactly where thermally altered
organic matter puts aromatic C=C — and jet and coal both derive from lignocellulose, while anthracite
retains essentially nothing else. The dominant feature of the Rhynie spectra is therefore a
**maturation** band, not a composition band.

This is the quantitative basis for the endmember-fitting result in
[`../analysis/endmember-fitting.md`](../analysis/endmember-fitting.md): fitting these references to
the Rhynie spectra returns the same mixture for every tissue regardless of what it was made of.
