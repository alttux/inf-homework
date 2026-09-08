from turtle import *
k = 30
# tracer(0)
left(90)
penup()
for _ in range(7):
    right(60)
    forward(k*9)
pendown()
for _ in range(5):
    forward(k*3)
    right(90)
for _ in range(8):
    right(30)
    forward(10*k)
    right(60)
penup()
for x in range(-5, 15):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(2, 'red')

done()