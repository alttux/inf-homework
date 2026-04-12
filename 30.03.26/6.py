from turtle import *

scale = 35
tracer(0)
left(90)
pendown()
for _ in range(2):
    forward(3 * scale)
    left(90)
    back(10 * scale)
    left(90)
penup()
back(10 * scale)
right(90)
forward(8 * scale)
left(90)
pendown()
for _ in range(2):
    forward(16 * scale)
    right(90)
    forward(8 * scale)
    right(90)
penup()
for x in range(-20, 25):
    for y in range(-15, 10):
        setpos(x*scale, y*scale)
        dot(2)


done()
