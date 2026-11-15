from turtle import *


tracer(0)
screensize(2000, 2000)
k = 15

left(90)

for _ in range(3):
    forward(18*k)
    right(90)
    forward(25*k)
    right(90)

penup()
forward(6*k)
right(90)
forward(9*k)
left(90)
pendown()

for _ in range(3):
    forward(30*k)
    right(90)
    forward(21*k)
    right(90)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*k, y*k)
        dot(1, 'red')

done()