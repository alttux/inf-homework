from math import ceil, log2

for N in range(1, 1000):
    l = 283
    i = ceil(log2(N))
    V1 = ceil(l*i/8)
    V65536 = V1 * 65_536
    if V65536 > (15*1024*1024):
        print(N)