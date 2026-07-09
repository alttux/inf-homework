n = [int(s) for s in open('files/9e838f1f-6733-459b-9d4c-f3bf68fd28ac_17.5.txt')]
out = []
for i in range(len(n)-1):
    para = n[i:i+2]
    if sum(para)>200 and any(x<0 for x in para):
        out.append(para[0]*para[1])
print(len(out), max(out))
