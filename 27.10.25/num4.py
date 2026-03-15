from turtle import *

k = 20
tracer(0)

left(90)
pendown()
# begin_fill()
for i in range(4):
    fd(10*k)
    rt(90)
# end_fill()
penup()
canvas = getcanvas()
count = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        # if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
        #     count += 1
        goto(x*k, y*k)
        dot(2, 'red')
print(count)
done()
# 81