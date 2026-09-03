import numpy as np
from scipy import ndimage as ndi

def draw_seg(vol, a, b, r, vox, lo, noise=0.0, rng=None):
    """Rasterise a cylinder from a to b of radius r into a boolean volume."""
    a=np.asarray(a,float); b=np.asarray(b,float)
    L=np.linalg.norm(b-a)
    n=max(2,int(L/(vox*0.4)))
    for t in np.linspace(0,1,n):
        c=a+(b-a)*t
        rr=r*(1.0+noise*rng.normal()) if noise else r
        ci=((c-lo)/vox).astype(int)
        rad=int(np.ceil(rr/vox))
        sl=tuple(slice(max(0,ci[k]-rad),min(vol.shape[k],ci[k]+rad+1)) for k in range(3))
        if any(s.stop<=s.start for s in sl): continue
        gg=np.mgrid[sl]
        d2=sum((gg[k]*vox+lo[k]-c[k])**2 for k in range(3))
        vol[sl] |= d2 <= rr*rr

def tree(rng, depth=7, r0=0.013, taper=0.92, seglen=0.22, spread=0.55):
    """Hierarchical bifurcating tree: a strict tree, zero cycles by construction."""
    segs=[]; 
    def rec(p, d, r, lvl):
        if lvl>=depth or r<0.004: return
        for _ in range(2):
            nd=d+rng.normal(0,spread,3); nd/=np.linalg.norm(nd)
            q=p+nd*seglen*(0.8+0.4*rng.random())
            segs.append((p,q,r))
            rec(q, nd, r*taper, lvl+1)
    rec(np.array([0.,0.,0.]), np.array([0.,0.,1.]), r0, 0)
    return segs

def reticulate(rng, n_nodes=90, r=0.0095, k=3, box=1.2):
    """Randomly anastomosing network: many cycles by construction."""
    P=rng.random((n_nodes,3))*box
    segs=[]; seen=set()
    for i in range(n_nodes):
        d=np.linalg.norm(P-P[i],axis=1); order=np.argsort(d)[1:k+1]
        for j in order:
            key=(min(i,j),max(i,j))
            if key in seen: continue
            seen.add(key); segs.append((P[i],P[j],r))
    return segs

def build(segs, vox=0.004, noise=0.0, seed=0, pad=10):
    rng=np.random.default_rng(seed)
    pts=np.array([p for s in segs for p in (s[0],s[1])])
    rmax=max(s[2] for s in segs)
    lo=pts.min(0)-pad*vox-rmax; hi=pts.max(0)+pad*vox+rmax
    shape=tuple((np.ceil((hi-lo)/vox).astype(int)+1).tolist())
    vol=np.zeros(shape,bool)
    for a,b,r in segs: draw_seg(vol,a,b,r,vox,lo,noise,rng)
    if noise>0:
        # surface roughness: random erosion/dilation at the boundary
        pert=rng.random(shape)
        edge=vol ^ ndi.binary_erosion(vol)
        vol=vol & ~(edge & (pert<noise*1.2))
        edge2=ndi.binary_dilation(vol) ^ vol
        vol=vol | (edge2 & (pert>1-noise*1.2))
    return vol, lo
