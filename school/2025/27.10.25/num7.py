from turtle import *

scale = 35
tracer(0.5)
pendown()
left(90)

for i in range(4):
    fd(10*scale)
    rt(90)
rt(30)
for i in range(4):
    fd(6*scale)
    rt(60)
    fd(6*scale)
    rt(120)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*scale, y*scale)
        dot(1, 'red')
done()
# 51