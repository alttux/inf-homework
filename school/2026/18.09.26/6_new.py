from turtle import *

k = 1.5
perim = 0
tracer(0)
left(90)

def fwd(n):
    global perim
    forward(n * k)
    perim += n

for _ in range(2):
    for _ in range(2):
        fwd(190)
        right(120)
    right(120)

right(150);
fwd(13)
right(90)
fwd(380)
right(90)
fwd(13)

right(30)
color('red')
fwd(67)
color('black')
perim -= 67  # не часть контура
print(perim)
done()
