from turtle import *

scale = 35
tracer(0)
left(90)
pendown()
for i in range(24):
    forward(3 * scale)
    left(60)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*scale, y*scale)
        dot(2)


done()
