from turtle import *

k = 100
tracer(0)
begin_fill()
for i in range(2):
    forward(8 * k)
    rt(150)
    fd(8*k)
    rt(30)
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

# 24