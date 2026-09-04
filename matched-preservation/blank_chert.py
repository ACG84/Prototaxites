"""Controls on the Rhynie ATR-FTIR data using blank chert from the same sections.

Loron et al. (2023, Nat Commun 14:1387) deposited their 53 raw ATR-FTIR spectra at
Edinburgh DataShare (https://datashare.ed.ac.uk/handle/10283/4797, CC BY).  Four of
them are *pure chert matrix* - no fossil - measured on the same instrument, in the
same sessions, on the same thin sections.  Those four are the taphonomically matched
mineral reference this project had been missing; the other 49 are duplicated in the
2026 Sci Adv Data S1.

Three controls are run here:

  1. How much of each fossil spectrum is chert?
  2. Igisu et al.'s (2009) null test - subtract one blank chert from another and see
     what "bands" appear.  A matrix subtraction that cannot pass this cannot be read.
  3. Where does blank chert fall in the fossil spectral space, and on the axis that
     separates Prototaxites from Fungi?

Inputs:
  loron2023.pkl  - {'wn', 'S', 'names'} parsed from ATR_raw_spectra_Loronetal.xlsx
  loron_raw.pkl  - {'wn', 'S', 'labels'} parsed from the 2026 Data S1 spectra sheet

Usage:  python3 blank_chert.py [loron2023.pkl] [loron_raw.pkl]
"""
import sys, pickle, itertools
import numpy as np
from scipy.signal import savgol_filter, find_peaks
from scipy.stats import mannwhitneyu, kruskal, spearmanr
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# region used to scale the matrix reference: silica lattice plus the transparent window
FIT_REGIONS = [(650, 900), (1800, 2700)]
ORGANIC = (1350, 1800)
PROC_WINDOW = (1450.15, 2999.09)     # the window Loron et al.'s processed sheets use


def rubberband(x, y, n_anchor=64):
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
    return y - np.interp(x, [p[0] for p in hull], [p[1] for p in hull])


def mask_of(wn, regions):
    m = np.zeros_like(wn, dtype=bool)
    for lo, hi in regions:
        m |= (wn >= lo) & (wn <= hi)
    return m


def subtract_matrix(wn, target, ref, fit):
    """target - (a*ref + quadratic baseline), a and baseline fitted on `fit`."""
    X = np.column_stack([ref[fit], np.ones(fit.sum()),
                         wn[fit] / 1000, (wn[fit] / 1000) ** 2])
    c, *_ = np.linalg.lstsq(X, target[fit], rcond=None)
    return target - (c[0] * ref + c[1] + c[2] * wn / 1000 + c[3] * (wn / 1000) ** 2)


def top_bands(wn, y, lo, hi, n=5):
    w = (wn >= lo) & (wn <= hi)
    ys = savgol_filter(y[w], 11, 3)
    xx = wn[w]
    p, _ = find_peaks(ys, prominence=0.02 * np.ptp(ys))
    return sorted(round(float(xx[i]), 0) for i in sorted(p, key=lambda i: -ys[i])[:n])


def processed(wn, s):
    """Approximation of the authors' D-sheet processing: rubberband + min-max."""
    w = (wn >= PROC_WINDOW[0]) & (wn <= PROC_WINDOW[1])
    v = rubberband(wn[w], s[w])
    return (v - v.min()) / (v.max() - v.min())


def main(p2023, p2026):
    d = pickle.load(open(p2023, 'rb'))
    wn, S23, names = d['wn'], d['S'], d['names']
    mi = [i for i, n in enumerate(names) if 'matrix' in n.lower()]
    M = S23[mi]
    lor = pickle.load(open(p2026, 'rb'))
    S, lab = lor['S'], np.array(lor['labels'])
    assert np.allclose(wn, lor['wn']), 'grids differ'
    groups = ['Bacteria', 'Amoeba', 'Arthropod', 'Fungi', 'Oomycete',
              'Plant', 'Plant spore', 'Prototaxites']

    print('=' * 72)
    print('1. How much of each fossil spectrum is chert?\n')
    Mm = M.mean(0)
    r = np.array([np.corrcoef(s, Mm)[0, 1] for s in S])
    for g in groups:
        v = r[lab == g]
        print(f'   {g:14s} n={len(v):3d}  r={v.mean():.4f}  [{v.min():.4f}, {v.max():.4f}]')
    print(f'\n   mean r^2 with blank chert: {np.mean(r ** 2):.3f}')
    print(f'   Kruskal-Wallis across groups: p={kruskal(*[r[lab == g] for g in groups]).pvalue:.3f}')
    print(f'   Prototaxites vs rest: p={mannwhitneyu(r[lab == "Prototaxites"], r[lab != "Prototaxites"]).pvalue:.3f}')

    print('\n' + '=' * 72)
    print('2. Null test - blank chert corrected against blank chert')
    print('   (Igisu et al. 2009 report no bands in 2300-1300 for their equivalent)\n')
    fit = mask_of(wn, FIT_REGIONS)
    org = (wn >= ORGANIC[0]) & (wn <= ORGANIC[1])
    null = []
    for a, b in itertools.permutations(range(len(M)), 2):
        res = subtract_matrix(wn, M[a], M[b], fit)
        null.append(np.ptp(res[org]))
        print(f'   {names[mi[a]][:18]:20s} - {names[mi[b]][:18]:20s} '
              f'ptp={null[-1]:.4f}  {top_bands(wn, res, *ORGANIC)}')
    print(f'\n   null amplitude range: {min(null):.4f} - {max(null):.4f}\n')
    print('   for comparison, matrix-corrected fossil group means:')
    for g in groups:
        R = np.array([subtract_matrix(wn, S[i], Mm, fit)
                      for i in np.where(lab == g)[0]]).mean(0)
        print(f'   {g:14s} ptp={np.ptp(R[org]):.4f}  {top_bands(wn, R, *ORGANIC)}')

    print('\n' + '=' * 72)
    print('3. Where does blank chert sit in the fossil spectral space?\n')
    F = np.array([processed(wn, s) for s in S])
    Mp = np.array([processed(wn, s) for s in M])
    pca = PCA(6).fit(F)
    Fp, Mq = pca.transform(F), pca.transform(Mp)
    mu, Ci = Fp.mean(0), np.linalg.pinv(np.cov(Fp.T))
    dm = lambda x: float(np.sqrt((x - mu) @ Ci @ (x - mu)))
    dF = np.array([dm(x) for x in Fp])
    print(f'   Mahalanobis to fossil centroid: fossils median {np.median(dF):.2f}, '
          f'max {dF.max():.2f}; blank chert {np.round([dm(x) for x in Mq], 2)}')

    sel = np.isin(lab, ['Prototaxites', 'Fungi'])
    ld = LDA().fit(Fp[sel], lab[sel])
    z, zm = ld.transform(Fp[sel])[:, 0], ld.transform(Mq)[:, 0]
    for g in ['Fungi', 'Prototaxites']:
        v = z[lab[sel] == g]
        print(f'   LD1 {g:13s} n={len(v):2d} mean {v.mean():+.2f} '
              f'range [{v.min():+.2f}, {v.max():+.2f}]')
    fu = z[lab[sel] == 'Fungi']
    print(f'   LD1 blank chert       n={len(zm)} values {np.round(zm, 2)} '
          f'-> inside the Fungi range: {sum(fu.min() <= q <= fu.max() for q in zm)}/{len(zm)}')

    D = np.sqrt(((Mp[:, None] - F[None]) ** 2).sum(-1)).min(1)
    DF = np.sqrt(((F[:, None] - F[None]) ** 2).sum(-1))
    np.fill_diagonal(DF, np.inf)
    print(f'   nearest-fossil distance for blank chert {np.round(D, 2)}; '
          f'fossil-to-fossil nearest neighbour median {np.median(DF.min(1)):.2f}, '
          f'max {DF.min(1).max():.2f}')

    print('\n   what does that axis track?')
    def ch_area(s):
        b = (wn >= 2800) & (wn <= 3000)
        sh = ((wn >= 2700) & (wn <= 2780)) | ((wn >= 3020) & (wn <= 3100))
        return np.trapezoid((s - np.polyval(np.polyfit(wn[sh], s[sh], 1), wn))[b], wn[b])
    ch = np.array([ch_area(s) for s in S])
    idx = np.where(sel)[0]
    print(f'   LD1 vs r-to-blank-chert   rho={spearmanr(z, r[idx])[0]:+.3f} '
          f'p={spearmanr(z, r[idx])[1]:.2g}')
    print(f'   LD1 vs C-H stretch area   rho={spearmanr(z, ch[idx])[0]:+.3f} '
          f'p={spearmanr(z, ch[idx])[1]:.2g}')
    print(f'   C-H area: Fungi {ch[lab == "Fungi"].mean():+.4f}, '
          f'Prototaxites {ch[lab == "Prototaxites"].mean():+.4f}, '
          f'p={mannwhitneyu(ch[lab == "Prototaxites"], ch[lab == "Fungi"]).pvalue:.4f}')


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else 'loron2023.pkl'
    b = sys.argv[2] if len(sys.argv) > 2 else 'loron_raw.pkl'
    main(a, b)
