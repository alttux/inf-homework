ns = [int(s) for s in open('files/17.4_O4Ymomn.txt')]
ns2x = []
for i in range(len(ns)-1):
    n1 = ns[i]
    n2 = ns[i+1]
    if n1>500 or n2>500:
        ns2x.append(n1**2+n2**2)
# print(ns2x)
print(len(ns2x), max(ns2x))