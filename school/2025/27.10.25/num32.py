from turtle import *

k = 120
tracer(0)
left(90)
pendown()
begin_fill()
for i in range(2):
    fd(7*k)
    rt(90)
    fd(8 * k)
    rt(90)
end_fill()
penup()
canvas = getcanvas()
count = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
            count += 1

print(count)
done()

#42