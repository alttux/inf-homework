from turtle import *
screensize(2000, 2000)
tracer(0)
k = 10
left(90)
for i in range(10):
    forward(9*k)
    right(90)
    forward(2*k)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(1, 'red')

done()