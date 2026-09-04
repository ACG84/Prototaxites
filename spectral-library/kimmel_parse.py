"""Extract spectra from a Spectragryph .sgdr database (reverse-engineered).

Layout, per record, little-endian float64 on an 8-byte alignment that is *not*
the file's own alignment (it is 7 bytes in the Kimmel and RRUFF files):

    ... , -1, -1, -1, -1, -1, -1, X_end, -step, -1, -1, -1, <6 filler>, y[0], y[1], ...

y runs from X_end downwards in constant steps.  The record is delimited by the
source-file path string that precedes it.

The six leading -1.0 sentinels followed by a plausible (X_end, -step) pair are a
specific enough signature to locate the header without assuming a fixed offset.
An earlier version of this parser assumed fixed indices 28/29; that held for 269
of the 363 Kimmel records and silently produced a nonsense axis for the other 94,
and shifted the axis of the rest by nine points (~17 cm^-1).  Hence the signature
search.

Validation (Kimmel library, this parser):
    Quartz            1084, 798/779, 513, 461      lit. 1085, 798/779, 512, 460
    Calcite            712, 875, 1423              lit.  712, 875, 1420
    Chitin            1658 (am I), 1556 (am II)    lit. 1660, 1556
    Collagen, fresh   1647 (am I), 1545 (am II)    lit. 1650, 1550

Usage:
    import kimmel_parse
    lib = kimmel_parse.load('Kimmel_Center_IR_spectra_library_363entries.sgdr')
    x, y = lib['Chitin (Crab shells Sigma)']
"""
import re
import numpy as np

# Source paths differ between databases; match any Windows path ending .SPA/.SPC/.DPT
PATH_RE = re.compile(rb"[A-Za-z]:\\[^\x00]{3,240}?\\([^\x00\\]{2,160}?)\.(?:SPA|SPC|DPT|TXT|CSV|ASC|JDX|DX)",
                     re.IGNORECASE)

ALIGNMENTS = range(8)
N_FILLER = 6          # doubles between the trailing -1 sentinels and y[0]
N_SENTINEL = 3        # -1 sentinels immediately after the step


def _header(a):
    """Index of X_end within float64 view `a`, or None."""
    is1 = (a == -1.0)
    for i in range(6, len(a) - 3):
        if (is1[i - 6:i].all() and not is1[i]
                and 500.0 < a[i] < 20000.0 and -20.0 < a[i + 1] < -0.001):
            return i
    return None


def _record(blob):
    for off in ALIGNMENTS:
        n = len(blob)
        a = np.frombuffer(blob[off:n - ((n - off) % 8)], dtype='<f8')
        i = _header(a)
        if i is None:
            continue
        end, step = float(a[i]), abs(float(a[i + 1]))
        seg = a[i + 1 + N_SENTINEL + N_FILLER + 1:]
        ok = np.isfinite(seg) & (seg > -2.0) & (seg < 50.0)
        j = 0
        while j < len(ok) and ok[j]:
            j += 1
        if j < 40:
            continue
        y = np.asarray(seg[:j], dtype=float)
        x = end - np.arange(j) * step
        if x[-1] < -50.0:                      # implausible axis
            continue
        o = np.argsort(x)
        return x[o], y[o]
    return None


def load(sgdr_path):
    """Return {name: (wavenumbers_ascending, absorbance)}."""
    d = open(sgdr_path, 'rb').read()
    pos = [(m.start(), m.group(1).decode('latin-1')) for m in PATH_RE.finditer(d)]
    out = {}
    for k, (start, name) in enumerate(pos):
        end = pos[k + 1][0] if k + 1 < len(pos) else len(d)
        r = _record(d[start:end])
        if r is not None:
            out[name] = r
    return out


if __name__ == '__main__':
    import sys, pickle
    src = sys.argv[1]
    lib = load(src)
    print(f'{len(lib)} spectra')
    bad = [k for k, (x, _) in lib.items() if x.max() - x.min() < 500]
    print(f'{len(bad)} with implausible axis span')
    if len(sys.argv) > 2:
        pickle.dump(lib, open(sys.argv[2], 'wb'))
