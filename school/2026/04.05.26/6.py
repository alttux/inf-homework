from turtle import *

from sympy.plotting.intervalmath import interval_arithmetic

k = 100

screensize(2000, 2000)
speed(1000)
# tracer(0)
left(90)

right(90)

begin_fill()
for i in range(3):
    forward(15*k)
    right(60)
    forward(10*k)
    right(60)
end_fill()
penup()
c=0
canvas = getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
            c+=1

print(c)

done()

# 392