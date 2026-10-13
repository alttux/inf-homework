a = [int(x) for x in open('17.txt').read().split()]
k = 0
mx = 0
for i in range(len(a) - 2):
    t = sorted(a[i:i+3])
    if t[0] + t[1] > t[2] and t[0]**2 + t[1]**2 > t[2]**2:  
        k += 1
        mx = max(mx, sum(t))
print(k, mx)   # 1175 29451