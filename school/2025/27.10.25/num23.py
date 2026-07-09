from turtle import *

k = 100
tracer(0)
left(90)
pendown()
begin_fill()
for i in range(7):
    forward(5 * k)
    left(60)
end_fill()
penup()
count = 0
canvas = getcanvas()

for x in range(-100, 100):
    for y in range(-100, 100):
        if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
            count += 1
print(count)
done()

# 62