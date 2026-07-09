from turtle import *

tracer(0)
k = 10

left(90)

right(315)
for i in range(7):
    forward(12*k)
    right(45)
    forward(6*k)
    right(135)
penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(2, 'red')


done()