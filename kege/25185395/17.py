n = [int(s) for s in open('xui.txt')]
out = []
ns = [l for l in n if l > 0 and l%123==0]
print(ns)
for i in range(len(n)-1):
    n1 = n[i]
    n2 = n[i+1]
    if  (n1+n2) < min(ns):
        out.append(n1+n2)

print(len(out), max(out))