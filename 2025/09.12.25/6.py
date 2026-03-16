from turtle import *

left(90)
screensize(2000, 2000)
tracer(0)
speed(1000)
k = 10
for i in range(3):
    forward(7 * k)
    right(90)
forward(10 * k)
for i in range(3):
    left(90)
    forward(6 * k)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(1, 'red')
done()
