import numpy as np, networkx as nx
from scipy import ndimage as ndi

NB = [(i,j,k) for i in(-1,0,1) for j in(-1,0,1) for k in(-1,0,1) if (i,j,k)!=(0,0,0)]

def skel_graph(sk, radius=None):
    """Build a centreline graph from a 3D skeleton. Nodes = tips/junctions."""
    pts = np.argwhere(sk)
    idx = {tuple(p): i for i, p in enumerate(pts)}
    adj = [[] for _ in pts]
    S = sk.shape
    for i, p in enumerate(pts):
        for d in NB:
            q = (p[0]+d[0], p[1]+d[1], p[2]+d[2])
            if 0 <= q[0] < S[0] and 0 <= q[1] < S[1] and 0 <= q[2] < S[2] and sk[q]:
                adj[i].append(idx[q])
    deg = np.array([len(a) for a in adj])
    nodemask = deg != 2
    G = nx.MultiGraph()
    for i in np.where(nodemask)[0]:
        G.add_node(i, pos=pts[i], r=(radius[tuple(pts[i])] if radius is not None else np.nan))
    seen = set()
    for i in np.where(nodemask)[0]:
        for nb in adj[i]:
            if (i, nb) in seen: continue
            path = [i, nb]; seen.add((i, nb)); seen.add((nb, i))
            prev, cur = i, nb
            while not nodemask[cur]:
                nxt = [a for a in adj[cur] if a != prev]
                if not nxt: break
                prev, cur = cur, nxt[0]
                seen.add((prev, cur)); seen.add((cur, prev))
                path.append(cur)
            L = sum(np.linalg.norm(pts[path[k+1]]-pts[path[k]]) for k in range(len(path)-1))
            G.add_edge(i, cur, length=L, path=path)
    return G, pts, adj, deg

def prune(G, pts, min_spur):
    """Remove short terminal spurs (skeletonisation artefacts)."""
    changed = True
    while changed:
        changed = False
        for n in list(G.nodes()):
            if G.degree(n) == 1:
                e = list(G.edges(n, data=True))[0]
                if e[2]['length'] < min_spur:
                    G.remove_edge(e[0], e[1], key=list(G[e[0]][e[1]].keys())[0])
                    changed = True
        G.remove_nodes_from([n for n in list(G.nodes()) if G.degree(n) == 0])
        # dissolve degree-2 nodes created by pruning
        for n in list(G.nodes()):
            if G.degree(n) == 2 and len(list(G.neighbors(n))) == 2:
                (a, _, da), (b, _, db) = [(u if u != n else v, None, d) for u, v, d in G.edges(n, data=True)]
                if a == b: continue
                G.add_edge(a, b, length=da['length']+db['length'], path=da['path']+db['path'])
                G.remove_node(n); changed = True
    return G

def betti1(G):
    """Cyclomatic number: independent loops. 0 for a tree."""
    return G.number_of_edges() - G.number_of_nodes() + nx.number_connected_components(G)

def edge_dir(G, u, v, k, pts, arc=8):
    """Unit direction leaving node u along edge (u,v,k), averaged over `arc` voxels."""
    path = G[u][v][k]['path']
    p = np.array(path)
    if np.array_equal(pts[path[0]], pts[u]) is False and path[0] != u:
        p = p[::-1]
    seg = pts[p[:min(arc, len(p))]]
    if len(seg) < 2: return None
    d = seg[-1].astype(float) - seg[0].astype(float)
    n = np.linalg.norm(d)
    return d/n if n > 0 else None

def junction_angles(G, pts, arc=8):
    out = []
    for n in G.nodes():
        if G.degree(n) < 3: continue
        dirs = []
        for u, v, k in G.edges(n, keys=True):
            other = v if u == n else u
            d = edge_dir(G, n, other, k, pts, arc) if G.has_edge(n, other) else None
            if d is not None: dirs.append(d)
        for i in range(len(dirs)):
            for j in range(i+1, len(dirs)):
                c = float(np.clip(np.dot(dirs[i], dirs[j]), -1, 1))
                out.append(np.degrees(np.arccos(c)))
    return np.array(out)
