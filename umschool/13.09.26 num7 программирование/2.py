from math import ceil, log2

h = 1024
w = 2048
n = 1024
v = 524_288

i = ceil(log2(n))

for k in range(1, 1000):
    t = (h * w * i * k) / v
    if t <= 320:
        print(k)