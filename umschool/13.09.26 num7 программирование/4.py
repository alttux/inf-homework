h = 1024
w = 512
k = 256
v = 6_393_911

for i in range(1, 1000):
    t = (h * w * i * k) / v
    if t <= 160:
        print(2**i)