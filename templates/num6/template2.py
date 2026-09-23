from turtle import *

k = 35
count = 0
left(90)
tracer(0)
pendown()
begin_fill()
for i in range(6):
    forward(3 * k)
    left(60)
end_fill()
penup()

canvas = getcanvas()

for x in range(-10, 10):
    for y in range(-10, 10):
        if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
            count += 1

print(count)
done()
