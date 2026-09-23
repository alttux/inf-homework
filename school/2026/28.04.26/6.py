from turtle import *

k = 10
left(90)
tracer(0)
for i in range(7):
    forward(15*k)
    right(90)
    forward(23*k)
    right(90)

penup()

forward(3*k)
right(90)
forward(5*k)
left(90)

pendown()

for i in range(7):
    forward(252*k)
    right(90)
    forward(398*k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(1, 'red')
done()

# 247