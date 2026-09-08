import math

x, y = 0.0, 0.0
angle = 90.0
segs = []

def fwd(n):
    global x, y
    nx = x + n * math.cos(math.radians(angle))
    ny = y + n * math.sin(math.radians(angle))
    segs.append(n)
    x, y = nx, ny

def right(d):
    global angle
    angle -= d

for _ in range(2):
    for _ in range(2):
        fwd(190)
        right(120)
    right(120)

right(150); fwd(13)
right(90);  fwd(380)
right(90);  fwd(13)
right(30);  fwd(67)

# отрезок 8 (67) — перерисовывает часть отрезка 1, не входит в периметр контура
print(sum(segs) - 67)  # 1166
