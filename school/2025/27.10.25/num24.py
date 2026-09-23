from turtle import *

scale = 10
speed(10000)
tracer(0)
screensize(2000, 2000)
pendown()
for i in range(9):
    forward(18 * scale)
    rt(72)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*scale, y*scale)
        dot(2)

done()

# 18