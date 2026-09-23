n = [int(s) for s in open('files/17.7_6fADpmL.txt')]
out = []
for i in range(len(n)-2):
    troi = n[i:i+3]
    if all(i < 0 for i in troi):
        out.append(sum(troi))

print(len(out), min(out))