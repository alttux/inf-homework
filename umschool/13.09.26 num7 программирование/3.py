from math import ceil, log2

h = 1024
w = 1024
k = 32
v = 1_474_560

for i in range(1, 1000):
    t = (h * w * i * k) / v
    if t <= 120:
        print(2**i)