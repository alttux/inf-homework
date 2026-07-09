n = [int(s) for s in open('files/17_DGqtUU5.txt')]
out = []
for i in range(len(n)-1):
    n1 = n[i]
    n2 = n[i+1]
    if abs(n1)+abs(n2)>700:
        out.append(n1)
        out.append(n2)
# print(len(out), max(out))
print(len(out)//2, max(out))