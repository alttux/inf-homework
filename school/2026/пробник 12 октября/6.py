from turtle import *

scale = 35
tracer(0)
left(90)
pendown()

for i in range(2):
    forward(3 * scale)
    left(90)
    backward(10 * scale)
    left(90)

penup()
backward(3 * scale)
right(90)
forward(8 * scale)
left(90)
pendown()

for i in range(2):
    forward(16 * scale)
    right(90)
    forward(8 * scale)
    right(90)

penup()

for x in range(-10, 20):
    for y in range(-10, 20):
        setpos(x*scale, y*scale)
        dot(2)

k = 0
for x in range(-10, 20):
    for y in range(-10, 20):
        if (0 <= x <= 9 and 0 <= y <= 2) or (8 <= x <= 15 and -3 <= y <= 12):
            k += 1

print(k)
done()