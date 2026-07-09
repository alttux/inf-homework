from turtle import *
tracer(0)
k = 10
left(90)


right(45)
for _ in range(3):
    right(45)
    forward(10*k)
    right(45)

right(315)
forward(10*k)
right(90)

forward(20*k)
right(90)

for _ in range(2):
    forward(10*k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(1, 'red')

done()