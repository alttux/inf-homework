from turtle import *

k = 20
tracer(0)
left(90)
pendown()
for i in range(4):
    fd(14*k)
    rt(90)
for i in range(5):
    fd(5*k)
    rt(45)
penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(1, 'red')

done()
#59