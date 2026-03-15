from turtle import *

k = 30
count = 0
tracer(0)

left(90)

pendown()
# begin_fill()
for i in range(2):
    forward(9*k)
    right(90)
    forward(15*k)
    right(90)
# end_fill()
penup()
forward(12)
right(90)
pendown()
# begin_fill()
for i in range(2):
    forward(6*k)
    right(90)
    forward(12*k)
    right(90)
# end_fill()
penup()


for x in range(-500, 500):
    for y in range(-500, 500):
        setpos(x*k, y*k)
        dot(2)

print(count) # 112
done()