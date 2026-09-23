from math import ceil, log2

hw = 1920*1920
n = 16_384
i = ceil(log2(n))
v = 1_474_560

for k in range(1, 1000):
    t = (hw * i * k) / v
    if t <= 280:
        print(k)

# n = 1920 * 1920
# i = ceil(log2(16_384))
# v = n * i
# V = 1474560 * 280
# print(V / v)