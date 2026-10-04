a = [int(x) for x in open('17-1.txt')]
m = max(a)
c = 0
s = float('inf')
for i in range(len(a) - 1):
    if a[i] + a[i+1] == m:
        c += 1
        s = min(s, a[i]**2)
print(f"{c}{s}")