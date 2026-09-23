from math import ceil, log2

for l in range(1, 10000):
    N = 10 + 52 + 5000
    i = ceil(log2(N))
    V1 = ceil(l * i / 8)
    V949 = V1 * 949
    if (V949 / 1024) > 727:
        print(l)
        break
