from turtle import *

scale = 10
# tracer(0)
screensize(2000, 200)

pendown()
for i in range(11):
    fd(36*scale)
    rt(72)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*scale, y*scale)
        dot(2)


done()

#36