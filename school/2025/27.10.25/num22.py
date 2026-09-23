from turtle import *

scale = 35
tracer(0.5)
# speed(1)
pendown()
left(90)

for i in range(4):
    for j in range(4):
        fd(8*scale)
        rt(90)
    fd(13*scale)
    rt(90)
    fd(4 * scale)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*scale, y*scale)
        dot(1, 'red')
done()
# 44
