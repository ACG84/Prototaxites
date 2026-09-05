"""Is the Prototaxites/Fungi contrast separable from thin-section provenance?

Data S2 of Loron et al. (2026) lists, for each of the 102 spectra, the specimen,
its England Finder coordinate and the **slide it came from**.  Parsing that gives
a provenance factor that can be crossed with the taxonomic labels.

It turns out that no slide contains both a Prototaxites spectrum and a fungal
one.  Taxon and slide are therefore perfectly aliased for the comparison that
carries the paper's central claim, and the tests below ask how much that matters:

  1. the group x slide contingency table;
  2. whether slide predicts the six published features *within a single taxon and
     a single tissue type* (plain Rhynia gwynne-vaughanii axes, n = 17);
  3. a slide-permutation null - split slides into two arbitrary groups of
     comparable size, ignoring taxonomy, and see how often that reproduces the
     observed feature gaps and the observed classification accuracy.

Inputs (not redistributed here; both are from the paper's Data S1/S2):
  spec_meta.json - {id: {desc, slide}} parsed from Data S2 by parse_s2()
  loron_raw.pkl  - {'wn', 'S', 'labels'} from the Data S1 'Raw spectra' sheet
  loron_cca.pkl  - {'feat', 'X'} from the Data S1 'CCA' sheet (102 x 6)

Usage:  python3 slide_confound.py [spec_meta.json] [loron_raw.pkl] [loron_cca.pkl]
"""
import sys, json, pickle, re, collections
import numpy as np
from scipy.stats import kruskal, mannwhitneyu
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score

SLIDE_NAMES = ['Lyon 156 UCB1', 'Lyon 48 UC1', 'Agl75 2019-1', 'Agl127 2019-2',
               'AgLyon 2019', 'RFf 2019', 'G.2024.5.5', 'G.2024.5.3', 'Agl204b',
               'NMSRC9', 'Agl127', '2892p', 'Agl2', 'Rfg', 'Rfe', 'Rfh']
GROUPS = ['Plant', 'Plant spore', 'Fungi', 'Bacteria', 'Arthropod',
          'Amoeba', 'Oomycete', 'Prototaxites']


def parse_s2(xlsx_path):
    """Parse Data S2 into {id: {'desc', 'slide'}}.

    The sheet is one column of free text in which several specimens are often run
    together on one line, so entries are split at standalone specimen numbers.
    Slide names containing digits ('Lyon 48 UC1') are masked first so they are not
    mistaken for specimen numbers.
    """
    import openpyxl
    ws = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True).worksheets[0]
    rows = [r[0] for r in ws.iter_rows(values_only=True) if r[0]]
    tok = {n: f'@{i}@' for i, n in enumerate(SLIDE_NAMES)}
    untok = {v: k for k, v in tok.items()}
    out = {}
    for r in rows[2:]:
        line = re.sub(r'\s+', ' ', str(r)).strip()
        for n in SLIDE_NAMES:                       # longest first
            line = re.sub(re.escape(n), tok[n], line, flags=re.I)
        marks = [(int(m.group(1)), m.start(), m.end())
                 for m in re.finditer(r'(?<![\w.\-@])(\d{1,3})\s+(?=[A-Za-z@])', line)]
        for i, (pid, _, end) in enumerate(marks):
            seg = line[end: marks[i + 1][1] if i + 1 < len(marks) else len(line)].strip()
            m = re.search(r'(@\d+@)\s*$', seg)
            out[pid] = {'desc': re.sub(r'@\d+@', lambda x: untok[x.group()], seg),
                        'slide': untok[m.group(1)] if m else None}
    return out


def ch_area(wn, s):
    """Aliphatic C-H stretch band area, local linear baseline."""
    b = (wn >= 2800) & (wn <= 3000)
    sh = ((wn >= 2700) & (wn <= 2780)) | ((wn >= 3020) & (wn <= 3100))
    return np.trapezoid((s - np.polyval(np.polyfit(wn[sh], s[sh], 1), wn))[b], wn[b])


def svm_accuracy(X, y, repeats=20):
    clf = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=10, gamma='scale'))
    cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=repeats, random_state=0)
    return cross_val_score(clf, X, y, cv=cv).mean()


def slide_split(slides, counts, rng, n_a=12, n_b=24):
    """Assign whole slides to two pseudo-groups of roughly n_a and n_b spectra."""
    A, B, na, nb = [], [], 0, 0
    for s in rng.permutation(slides):
        if na < n_a:
            A.append(s); na += counts[s]
        elif nb < n_b:
            B.append(s); nb += counts[s]
    return (A, B) if na >= 8 and nb >= 16 else (None, None)


def main(meta_path, raw_path, cca_path):
    meta = json.load(open(meta_path))
    lor = pickle.load(open(raw_path, 'rb'))
    wn, S, lab = lor['wn'], lor['S'], np.array(lor['labels'])
    cca = pickle.load(open(cca_path, 'rb'))
    X, feat = np.asarray(cca['X']), cca['feat']
    slide = np.array([meta[str(i)]['slide'] for i in range(len(lab))])
    desc = [meta[str(i)]['desc'] for i in range(len(lab))]

    print('=' * 74)
    print('1. Group x slide\n')
    tab = collections.defaultdict(collections.Counter)
    for i, l in enumerate(lab):
        tab[slide[i]][l] += 1
    print(f'{"slide":16s} ' + ' '.join(f'{g[:7]:>8s}' for g in GROUPS) + '   total')
    for s in sorted(tab, key=lambda s: -sum(tab[s].values())):
        print(f'{s:16s} ' + ' '.join(f'{tab[s][g] or "":>8}' for g in GROUPS)
              + f'   {sum(tab[s].values()):>5}')
    pro = {s for s in tab if tab[s]['Prototaxites']}
    fun = {s for s in tab if tab[s]['Fungi']}
    print(f'\n   Prototaxites slides: {sorted(pro)}')
    print(f'   Fungi slides:        {sorted(fun)}')
    print(f'   OVERLAP:             {sorted(pro & fun)}')

    print('\n' + '=' * 74)
    print('2. Slide effect within one taxon and one tissue type')
    print('   (plain Rhynia gwynne-vaughanii axes: no tracheids, cuticle or decayed axes)\n')
    sel = np.array([bool(re.match(r'Rhynia gwynne-?vaughanii\s+Plant', d)) for d in desc])
    ch = np.array([ch_area(wn, s) for s in S])
    by = {s: ch[sel & (slide == s)] for s in sorted(set(slide[sel]))}
    by = {k: v for k, v in by.items() if len(v) >= 2}
    print(f'   n = {sel.sum()} spectra, {len(by)} slides with n >= 2')
    for k, v in sorted(by.items(), key=lambda kv: -np.median(kv[1])):
        print(f'     {k:16s} n={len(v)}  C-H median {np.median(v):+.4f}  '
              f'[{v.min():+.4f}, {v.max():+.4f}]')

    gap = {f: abs(np.median(X[lab == 'Fungi', j]) - np.median(X[lab == 'Prototaxites', j]))
           for j, f in enumerate(feat)}
    print(f'\n   {"feature":28s} {"KW p":>8s} {"slide range":>12s} {"Proto-Fungi gap":>16s}')
    for j, f in enumerate(feat):
        g = {s: X[sel & (slide == s), j] for s in set(slide[sel])}
        g = {k: v for k, v in g.items() if len(v) >= 2}
        p = kruskal(*g.values()).pvalue
        rng_ = max(np.median(v) for v in g.values()) - min(np.median(v) for v in g.values())
        flag = '  <- slide range exceeds it' if rng_ > gap[f] else ''
        print(f'   {f[:28]:28s} {p:8.4f} {rng_:12.4f} {gap[f]:16.4f}{flag}')
    print('   (six tests; a Bonferroni threshold would be 0.0083 and none of these clears it)')

    print('\n' + '=' * 74)
    print('3. Slide-permutation null: arbitrary groups of slides, taxonomy ignored\n')
    rng = np.random.default_rng(0)
    slides = sorted(set(slide))
    counts = {s: int((slide == s).sum()) for s in slides}
    print(f'   {"feature":28s} {"observed":>9s} {"null med":>9s} {"null p95":>9s} {"p":>7s}')
    for j, f in enumerate(feat):
        v = X[:, j]
        null = []
        for _ in range(20000):
            A, B = slide_split(slides, counts, rng)
            if A is None:
                continue
            null.append(abs(np.median(v[np.isin(slide, A)]) - np.median(v[np.isin(slide, B)])))
        null = np.array(null)
        print(f'   {f[:28]:28s} {gap[f]:9.4f} {np.median(null):9.4f} '
              f'{np.percentile(null, 95):9.4f} {(null >= gap[f]).mean():7.3f}')

    m = np.isin(lab, ['Prototaxites', 'Fungi'])
    obs = svm_accuracy(X[m], lab[m])
    print(f'\n   Prototaxites vs Fungi on the six features: accuracy {obs:.3f} (baseline 0.667)')
    accs = []
    for _ in range(300):
        A, B = slide_split(slides, counts, rng)
        if A is None:
            continue
        ia, ib = np.isin(slide, A), np.isin(slide, B)
        accs.append(svm_accuracy(np.vstack([X[ia], X[ib]]),
                                 np.array(['A'] * ia.sum() + ['B'] * ib.sum()), repeats=6))
    accs = np.array(accs)
    print(f'   same classifier on {len(accs)} arbitrary slide-splits: median {np.median(accs):.3f}, '
          f'90th pct {np.percentile(accs, 90):.3f}, max {accs.max():.3f}')
    print(f'   fraction of slide-splits reaching >= {obs:.3f}: {(accs >= obs).mean():.3f}')


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else 'spec_meta.json'
    b = sys.argv[2] if len(sys.argv) > 2 else 'loron_raw.pkl'
    c = sys.argv[3] if len(sys.argv) > 3 else 'loron_cca.pkl'
    main(a, b, c)
