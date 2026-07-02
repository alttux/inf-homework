ns = [int(s) for s in open('files/61312418-f539-43ec-b4ab-b6b74a1b75f5_17.2.dz.txt')]
ns2x=[]
for i in range(len(ns)-1):
    n1 = ns[i]
    n2 = ns[i+1]
    if n1>0 and n1**(1/2)%1==0 or n2>0 and n2**(1/2)%1==0:
        ns2x.append(n1+n2)

print(len(ns2x), max(ns2x))