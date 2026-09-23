ns = [int(s) for s in open('files/17.6_PALix2J.txt')]
ns2x=[]
for i in range(len(ns)-2):
    n1 = ns[i]
    n2 = ns[i+1]
    n3 = ns[i+2]
    if n1<0 or n2<0 or n3<0:
        ns2x.append(n1+n2+n3)
print(len(ns2x), min(ns2x))