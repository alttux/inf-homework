from turtle import *

k = 10
tracer(0)
left(90)
pendown()

fillcolor('red')
for i in range(2):
    fd(9*k)
    rt(90)
    fd(15*k)
    rt(90)
pu()

fd(12*k)
rt(90)
pd()
for i in range(2):
    fd(6*k)
    rt(90)
    fd(12*k)
    rt(90)
pu()


for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(1, 'red')
done()
# 127