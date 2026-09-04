"""Choose the preprocessing for fit.py by internal control, not by eye.

For each of 28 combinations of derivative order, smoothing width and spectral
window, fit every Rhynie group mean as a non-negative mixture of the reference
endmembers, and record the rank the *correct* endmember receives for the groups
whose composition is known.  A preprocessing that cannot recover chitin from a
chitinous fossil cannot be trusted to say anything about Prototaxites.

Usage:  python3 sweep.py [kimmel_parsed.pkl] [loron_raw.pkl]
"""
import sys, pickle
import numpy as np
from scipy.signal import savgol_filter
from scipy.optimize import nnls

import fit as F

TRUTH = {
    'Arthropod': ['Chitin (Crab shells Sigma)'],
    'Fungi':     ['Chitin (Crab shells Sigma)'],
    'Plant':     ['Lignin', 'Cellulose', 'Wood (Pine fresh)'],
    'Bacteria':  ['Collagen (pure, fresh)', 'Keratin (fingernail)'],
}

WINDOW_SETS = [
    [(1350, 1800), (2800, 3050)],
    [(1500, 1800)],
    [(1350, 1800)],
    [(1200, 1800), (2800, 3050)],
]


def make_prep(wn, mode, width, windows):
    mask = np.zeros_like(wn, dtype=bool)
    for lo, hi in windows:
        mask |= (wn >= lo) & (wn <= hi)

    def prep(y):
        if mode == 'd2':
            v = savgol_filter(y, width, 3, deriv=2)
        elif mode == 'd1':
            v = savgol_filter(y, width, 3, deriv=1)
        else:
            v = F.rubberband(wn, savgol_filter(y, 7, 3))
        v = v[mask]
        v = v - v.mean()
        n = np.linalg.norm(v)
        return v / n if n > 0 else v

    return prep


def main(kimmel_pkl, loron_pkl):
    lib = pickle.load(open(kimmel_pkl, 'rb'))
    lor = pickle.load(open(loron_pkl, 'rb'))
    wn, S, labels = lor['wn'], lor['S'], lor['labels']
    names = [k for k in F.ENDMEMBERS if k in lib]

    variants = [(m, w, ws)
                for m in ('d2', 'd1', 'rb')
                for w in ((13, 21, 31) if m != 'rb' else (0,))
                for ws in WINDOW_SETS]

    hdr = ' | '.join(f'{g[:9]:>9s}' for g in TRUTH)
    print(f'{"mode":5s} {"w":>3s} {"windows":32s} | {hdr} | meanR2')
    print(f'{"":5s} {"":>3s} {"":32s} | ' +
          ' | '.join(f'{"rank/24":>9s}' for _ in TRUTH) + ' |')

    for mode, width, windows in variants:
        prep = make_prep(wn, mode, width, windows)
        E = np.array([prep(np.interp(wn, *lib[k])) for k in names]).T
        ranks, r2s = {}, []
        for g in list(TRUTH) + ['Prototaxites']:
            idx = [i for i, l in enumerate(labels) if l == g]
            t = prep(S[idx].mean(axis=0))
            w, _ = nnls(E, t)
            r2s.append(1 - np.sum((t - E @ w) ** 2) / np.sum((t - t.mean()) ** 2))
            if g in TRUTH:
                order = list(np.argsort(-w))
                ranks[g] = min(order.index(names.index(c))
                               for c in TRUTH[g] if c in names) + 1
        span = ','.join(f'{a:.0f}-{b:.0f}' for a, b in windows)
        print(f'{mode:5s} {width:3d} {span:32s} | '
              + ' | '.join(f'{ranks[g]:9d}' for g in TRUTH)
              + f' | {np.mean(r2s):.3f}')


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else 'kimmel_parsed.pkl'
    b = sys.argv[2] if len(sys.argv) > 2 else 'loron_raw.pkl'
    main(a, b)
