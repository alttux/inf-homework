from itertools import permutations, product
def F(w,x,y,z):
    return (not z and y and x and not w) or (not z and y and not x and not w) or (z and y and x and not w)
rows=[(None,1,None,None),(None,0,1,None),(0,None,0,None)]
def opt(r,p):
    fr=[i for i in range(4) if r[i] is None]; s=set()
    for f in product([0,1],repeat=len(fr)):
        v=list(r)
        for i,b in zip(fr,f): v[i]=b
        if F(*[v[p[k]] for k in range(4)]): s.add(tuple(v))
    return s
for p in permutations(range(4)):
    O=[opt(r,p) for r in rows]
    if any(not o for o in O): continue
    if any(len(set(q))==3 for q in product(*O)):
        r=['']*4
        for k in range(4): r[p[k]]='wxyz'[k]
        print(''.join(r))