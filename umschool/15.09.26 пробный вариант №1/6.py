from turtle import *
k = 10
tracer(0)
speed(2000)
screensize(2000, 2000)

left(90)

for _ in range(6):
    forward(k*28)
    right(90)
    forward(k*36)
    right(90)

penup()

forward(k*3)
right(90)
forward(k*12)
left(90)

pendown()

for _ in range(6):
    forward(k*64)
    right(90)
    forward(k*59)
    right(90)

penup()

for x in range(-10, 40):
    for y in range(-10, 30):
        goto(x*k, y*k)
        dot(1, 'red')

done()