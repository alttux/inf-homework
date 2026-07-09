n = [int(s) for s in open('files/17.4.1.txt')]
out = []
for i in range(len(n)-1):
    para = n[i:i+2]
    if sum(para)%2==0:
        # out.append(i)
        out.append(sum(para))
print(len(out), min(out))