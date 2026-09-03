import numpy as np
def bary_lattice(k):
    pts=[]
    for i in range(k+1):
        for j in range(k+1-i):
            pts.append((i/k,j/k,(k-i-j)/k))
    return np.array(pts)

def rasterize(V, F, vox, pad=6, chunk=400000):
    """Solid-surface voxelisation by barycentric supersampling of triangles."""
    P=V[F.reshape(-1)].reshape(-1,3,3)
    emax=np.max([np.linalg.norm(P[:,0]-P[:,1],axis=1),
                 np.linalg.norm(P[:,1]-P[:,2],axis=1),
                 np.linalg.norm(P[:,2]-P[:,0],axis=1)],axis=0)
    k=int(np.ceil(np.percentile(emax,99)/(vox*0.5)))
    k=max(1,min(k,8))
    B=bary_lattice(k)
    lo=V[np.unique(F)].min(0)-pad*vox; hi=V[np.unique(F)].max(0)+pad*vox
    shape=tuple((np.ceil((hi-lo)/vox).astype(int)+1).tolist())
    vol=np.zeros(shape,bool)
    for s in range(0,len(P),chunk):
        Q=P[s:s+chunk]
        pts=np.einsum('nb,tbc->ntc',B,Q).reshape(-1,3)
        idx=((pts-lo)/vox).astype(np.int32)
        np.clip(idx,0,np.array(shape)-1,out=idx)
        vol[idx[:,0],idx[:,1],idx[:,2]]=True
    return vol, lo, k
