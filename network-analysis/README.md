# Network topology analysis of the *Prototaxites taiti* medullary spot

Reproducible pipeline for the results in
[`../analysis/network-topology-results.md`](../analysis/network-topology-results.md).

## Getting the data

The 3D model is public. The DataShare landing page is JavaScript-rendered, but the DSpace REST API
serves the files directly:

```bash
# DOI 10.7488/ds/7895 resolves to item a20a7a8c-a9a2-4747-9649-0c2a8543e6c4
curl -sS "https://datashare.ed.ac.uk/server/api/core/items/a20a7a8c-a9a2-4747-9649-0c2a8543e6c4/bundles" \
  -H 'Accept: application/json'
# then for the ORIGINAL bundle:
curl -sS "https://datashare.ed.ac.uk/server/api/core/bundles/8cd9957c-21d5-492a-a9c8-43512cb3a499/bitstreams?size=200" \
  -H 'Accept: application/json'
# medullary spot model (248 MB):
curl -sSL -o spot_model.obj \
  "https://datashare.ed.ac.uk/server/api/core/bitstreams/a778ce72-82d1-4f11-acbb-b713aa1a4dec/content"
```

Other files in the deposit: the raw Airyscan confocal z-stack (1.48 GB TIFF, 114 slices, NMS
G.2024.5.7 / MPEG0057), three photogrammetry models of chert blocks, and 1.9 GB of microphotographs.

## Files

- `raster.py` — watertight solid voxelisation by barycentric supersampling of triangles.
  **Do not voxelise the vertex cloud**: median triangle edge is 0.0031 model units, so a vertex-only
  grid leaks below ~0.005 and manufactures spurious loops (see Results §2).
- `netlib.py` — skeleton → centreline graph, spur pruning, cyclomatic number, junction angles.

## Requirements

`numpy scipy scikit-image networkx`

## Known limitations

Read §4 of the results before using any number from this. The absolute loop count is **not**
resolution-stable; only large-circuit counts are. There is no matched-noise tree control, which is the
main thing needed to make the result defensible.
