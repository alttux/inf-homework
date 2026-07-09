from turtle import *

k = 10
count = 0

tracer(0)
pendown()
left(90)
begin_fill()
for i in range(2):
    forward(8 * k)
    right(60)
    forward(8 * k)
    right(120)
end_fill()
penup()

canvas = getcanvas()

for x in range(-100, 100):
    for y in range(-100, 100):
        if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
            count += 1
print(count)
done()

# 48