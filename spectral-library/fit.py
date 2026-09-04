"""Endmember fitting of the Loron et al. (2026) Rhynie spectra against reference
materials from the Kimmel Center IR library.

Two things make a naive fit meaningless and are handled explicitly:

  * the Rhynie spectra are ATR on a silica matrix, so Si-O dominates 1000-1250
    cm^-1 and swamps every organic band;
  * ATR and KBr-transmission spectra differ in baseline and in the wavelength
    dependence of penetration depth.

Preprocessing is rubberband baseline removal followed by vector normalisation
over organic-diagnostic windows.  That combination was not chosen by eye: see
sweep.py, which scores 28 preprocessing variants by whether Rhynie tissues of
known composition recover their own endmember.

The point of the exercise is not the best match for Prototaxites on its own.
It is whether the *other seven* Rhynie groups - tissues of known composition -
recover sensible endmembers.  They do not.  See ../analysis/endmember-fitting.md.

Usage:  python3 fit.py [kimmel_parsed.pkl] [loron_raw.pkl]
"""
import sys, pickle
import numpy as np
from scipy.signal import savgol_filter
from scipy.optimize import nnls

# Organic-diagnostic windows.  1350-1800 carries amide I/II, C=O, aromatic C=C
# and the carboxylate bands; 2800-3050 carries aliphatic and aromatic C-H.
# The 1000-1250 silica region is excluded outright.
WINDOWS = [(1350.0, 1800.0), (2800.0, 3050.0)]

# Curated endmembers.  Names must match keys in the parsed Kimmel dictionary.
ENDMEMBERS = {
    # mineral matrix
    'Quartz':                                    'mineral',
    'Flint':                                     'mineral (chert)',
    'Calcite geological spar':                   'mineral',
    'Kaolinite (Guyong, China)':                 'mineral (clay)',
    # modern biopolymers
    'Chitin (Crab shells Sigma)':                'modern - chitin',
    'Cellulose':                                 'modern - cellulose',
    'Lignin':                                    'modern - lignin',
    'Starch':                                    'modern - starch',
    'Collagen (pure, fresh)':                    'modern - protein',
    'Keratin (fingernail)':                      'modern - protein',
    'Wood (Pine fresh)':                         'modern - lignocellulose',
    'Resin tree modern Pisticia lentiscus':      'modern - terpenoid resin',
    # buried / Quaternary
    'Humic Acid (Huleh peat, A. Nissenbaum)':    'Holocene - humified OM',
    'Charcoal (Wood fresh)':                     'charred lignocellulose',
    'Wood fossil (Untreated) Cave of Letters 3916': 'Roman - buried wood',
    'Collagen (fossil  more than 50,000 BP)':    'Pleistocene - protein',
    'Copal (Philippines, A. Nissenbaum)':        'sub-fossil resin',
    # deep time
    'Amber (Dominican Republic, A. Nissenbaum)': 'Miocene resin ~20 Ma',
    'Amber (Baltic, A. Nissenbaum)':             'Eocene resin ~40 Ma',
    'Amber (New Jersey, A. Nissenbaum)':         'Cretaceous resin ~90 Ma',
    'Jet (England, A. Nissenbaum)':              'Jurassic coalified wood ~180 Ma',
    'Coal ':                                     'Carboniferous coal',
    'Anthracite (coal) (Wards)':                 'anthracite, high rank',
    'Bitumen (Oman 1927, Nissenbaum)':           'migrated hydrocarbon',
}


# Two window sets.  The wide one gives the best fit quality; the narrow one
# forces the fit onto the organic region by excluding the silica shoulder.
WINDOW_SETS = [
    ('organic only', [(1500.0, 1800.0)]),
    ('wide',         [(1200.0, 1800.0), (2800.0, 3050.0)]),
]

GROUP_ORDER = ['Bacteria', 'Amoeba', 'Arthropod', 'Fungi', 'Oomycete',
               'Plant', 'Plant spore', 'Prototaxites']


def rubberband(x, y, n_anchor=64):
    """Subtract the lower convex hull, evaluated on n_anchor sample points."""
    idx = np.linspace(0, len(x) - 1, n_anchor).astype(int)
    hull = []
    for px, py in ((x[i], y[i]) for i in idx):
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            if (y2 - y1) * (px - x1) >= (py - y1) * (x2 - x1):
                hull.pop()
            else:
                break
        hull.append((px, py))
    hx = np.array([p[0] for p in hull])
    hy = np.array([p[1] for p in hull])
    return y - np.interp(x, hx, hy)


def prep(wn, y, mask):
    v = rubberband(wn, savgol_filter(y, 7, 3))[mask]
    v = v - v.mean()
    n = np.linalg.norm(v)
    return v / n if n > 0 else v


def main(kimmel_pkl, loron_pkl):
    lib = pickle.load(open(kimmel_pkl, 'rb'))
    lor = pickle.load(open(loron_pkl, 'rb'))
    wn, S, labels = lor['wn'], lor['S'], lor['labels']

    missing = [k for k in ENDMEMBERS if k not in lib]
    if missing:
        print('WARNING: endmembers not in library:', missing, '\n')
    names = [k for k in ENDMEMBERS if k in lib]

    groups = ([g for g in GROUP_ORDER if g in set(labels)]
              + [g for g in sorted(set(labels)) if g not in GROUP_ORDER])

    for tag, windows in WINDOW_SETS:
        mask = np.zeros_like(wn, dtype=bool)
        for lo, hi in windows:
            mask |= (wn >= lo) & (wn <= hi)
        E = np.array([prep(wn, np.interp(wn, *lib[k]), mask) for k in names]).T

        span = ', '.join(f'{a:.0f}-{b:.0f}' for a, b in windows)
        print('=' * 72)
        print(f'{tag}: {len(names)} endmembers, {mask.sum()} points ({span} cm-1)\n')
        for g in groups:
            idx = [i for i, l in enumerate(labels) if l == g]
            t = prep(wn, S[idx].mean(axis=0), mask)
            w, _ = nnls(E, t)
            r2 = 1.0 - np.sum((t - E @ w) ** 2) / np.sum((t - t.mean()) ** 2)
            tot = w.sum() or 1.0
            print(f'--- {g}  (n={len(idx)})   R2 = {r2:.3f}')
            for j in np.argsort(-w)[:5]:
                if w[j] <= 1e-9:
                    continue
                print(f'      {100 * w[j] / tot:5.1f}%  {names[j][:44]:46s} '
                      f'[{ENDMEMBERS[names[j]]}]')
            print()


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else 'kimmel_parsed.pkl'
    b = sys.argv[2] if len(sys.argv) > 2 else 'loron_raw.pkl'
    main(a, b)
