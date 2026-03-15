from turtle import *

k = 100
tracer(0)
left(90)
pendown()
begin_fill()
for i in range(4):
    fd(12 * k)
    rt(90)
end_fill()
fillcolor('red')
begin_fill()
for i in range(3):
    fd(12 * k)
    rt(120)
end_fill()
penup()
canvas = getcanvas()
count = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        # goto(x*k, y*k)
        # dot(2, 'green')
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            count += 1
        # print(canvas.find_overlapping(x*k, y*k, x*k, y*k))
print(count)
done()

# /usr/local/bin/python3.13
# 65
