from turtle import *

scale = 35
tracer(0.6)
# speed(1000)
screensize(2000, 2000)

pendown()

for i in range(9):
    fd(22*scale)
    rt(90)
    fd(6*scale)
    rt(90)
penup()
fd(1*scale)
rt(90)
fd(5*scale)
lt(90)
pendown()
for i in range(9):
    fd(53*scale)
    rt(90)
    fd(75*scale)
    rt(90)
penup()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*scale, y*scale)
        dot(1, 'red')

done()

# 44