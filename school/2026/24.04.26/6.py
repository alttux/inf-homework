from turtle import *

k = 20
tracer(0)
left(90)

for i in range(4):
    forward(12*k)
    right(150)
    forward(12*k)
    right(30)

penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(1, 'red')

done()

# 59