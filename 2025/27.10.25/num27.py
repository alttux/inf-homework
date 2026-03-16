from turtle import *

k = 35
speed(10000)
tracer(0)
left(90)
pendown()

for i in range(2):
    fd(9*k)
    rt(90)
    fd(15*k)
    rt(90)

penup()
fd(12*k)
rt(90)
pendown()

for i in range(2):
    fd(6*k)
    rt(90)
    fd(12*k)
    rt(90)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*k, y*k)
        dot(1, 'red')

done()

# 70