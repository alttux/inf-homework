from turtle import *


k = 15
screensize(2000, 2000)
tracer(0)

left(90)

for _ in range(2):
    forward(12*k)
    left(270)
    forward(15*k)
    right(90)

penup()

backward(5*k)
right(90)
forward(9*k)
left(90)

pendown()

for _ in range(2):
    forward(14*k)
    right(90)
    forward(10*k)
    right(90)

penup()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x*k, y*k)
        dot(1, 'red')

print(12*15+14*10-6*9)

done()