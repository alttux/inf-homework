from turtle import *
k = 15
screensize(2000, 2000)
tracer(0)

left(90)
for _ in range(4):
    forward(6*k)
    right(90)
    forward(6*k)
    left(90)
    forward(6*k)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(1, 'red')

done()