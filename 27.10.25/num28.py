from turtle import *

k = 10
count = 0
left(90)
tracer(0)
pendown()
begin_fill()
for i in range(3):
    forward(13 * k)
    rt(120)
end_fill()
penup()

canvas = getcanvas()

for x in range(-100, 100):
    for y in range(-100, 100):
        if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
            count += 1

print(count)
done()

# 66