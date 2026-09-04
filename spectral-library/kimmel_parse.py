"""
Extract the Kimmel Center IR spectral library from Spectragryph's .sgdr format.

Source: Kimmel Center for Archaeological Science, Weizmann Institute (Prof. Steven Weiner)
        "FTIR spectra of natural and biogenic materials, as occurring in archaeological sciences"
Mirror: https://www.effemm2.de/spectragryph/databases/Kimmel_Center_IR_spectra_library_363entries.zip
Origin: http://www.weizmann.ac.il/kimmel-arch/infrared-spectra-library

Format, reverse-engineered:
  - Entries are delimited by the original Windows path string ending ".SPA"
  - Each entry's numeric block is float64 little-endian, found by scanning the 8 byte
    alignments for the longest run of finite values with |v| < 1e5
  - Within that block: index 28 = END wavenumber, index 29 = NEGATIVE step,
    data begins at index 30 and runs toward LOW wavenumber
  - Reconstructed axis: x[i] = v[28] - i * |v[29]|

Validated against known band positions: quartz 1066/781/762, chitin amide I 1641 /
amide II 1539, fresh collagen 1633/1531/1223, cellulose 1041/1095/1147.
"""
import re, numpy as np

PATH_RE = rb"C:\\Data\\Delphi\\work\\SpectralDatabases\\Kimmel_IR\\spectra\\([^\x00]{3,120}?)\.SPA"

def _longest_float_run(seg, min_len=300):
    best = None
    for al in range(8):
        n = (len(seg) - al) // 8
        if n < min_len:
            continue
        a = np.frombuffer(seg[al:al + n * 8], dtype='<f8')
        good = np.isfinite(a) & (np.abs(a) < 1e5)
        idx = np.flatnonzero(~good)
        bounds = np.concatenate(([-1], idx, [len(a)]))
        gaps = np.diff(bounds) - 1
        k = int(np.argmax(gaps))
        L = int(gaps[k])
        if L < min_len:
            continue
        if best is None or L > best[0]:
            best = (L, a[int(bounds[k]) + 1:int(bounds[k]) + 1 + L])
    return None if best is None else best[1]

def load(sgdr_path):
    """Return {name: (wavenumbers_ascending, absorbance)}."""
    d = open(sgdr_path, 'rb').read()
    pos = [(m.start(), m.group(1).decode('latin-1')) for m in re.finditer(PATH_RE, d)]
    out = {}
    for i, (st, name) in enumerate(pos):
        en = pos[i + 1][0] if i + 1 < len(pos) else len(d)
        v = _longest_float_run(d[st:en])
        if v is None or len(v) < 40:
            continue
        end, step = float(v[28]), abs(float(v[29]))
        y = np.asarray(v[30:], dtype=float)
        x = end - np.arange(len(y)) * step
        o = np.argsort(x)
        out[name] = (x[o], y[o])
    return out

if __name__ == "__main__":
    import sys, pickle
    lib = load(sys.argv[1])
    print(f"{len(lib)} spectra")
    pickle.dump(lib, open("kimmel_parsed.pkl", "wb"))
