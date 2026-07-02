ns = [int(s) for s in open('files/17.1_XrCwPYS.txt')]
ns2x = []
for i in range(len(ns)-1):
    n1 = ns[i]
    n2 = ns[i+1]
    if n1%8==0 and n2%8==0:
        ns2x.append(abs(n1-n2))

print(len(ns2x), min(ns2x))