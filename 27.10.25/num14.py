from itertools import count
from turtle import *

scale = 35
tracer(0.5)
left(90)
pendown()
begin_fill()
for i in range(2):
    fd(3*scale)
    lt(90)
    backward(10*scale)
    lt(90)
end_fill()
penup()
backward(10*scale)
right(90)
forward(8*scale)
lt(90)
pendown()
begin_fill()
for i in range(2):
    forward(16*scale)
    rt(90)
    fd(8*scale)
    rt(90)
end_fill()
penup()
count = 0
cv = getcanvas()
for x in range(-20, 20):
    for y in range(-20, 20):
        if cv.find_overlapping(x*scale, y*scale, x*scale, y*scale) != ():
            count+=1
print(count)
done()

# 185