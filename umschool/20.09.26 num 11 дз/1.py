from math import ceil, log2

for l in range(1000, 1, -1):
    N = 52 + 980
    i = ceil(log2(N))
    V1 = ceil(l * i / 8)
    V385 = V1 * 385
    if (V385 / 1024) < 136:
        print(l)
        break