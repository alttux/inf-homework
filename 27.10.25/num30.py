from turtle import *

k = 200
tracer(0)
left(90)
pendown()
begin_fill()
for i in range(3):
    fd(7*k)
    rt(120)
end_fill()
penup()
canvas = getcanvas()
count = 0
for x in range(-600, 600):
    for y in range(-600, 600):
        if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
            count += 1

print(count)
done()

#18