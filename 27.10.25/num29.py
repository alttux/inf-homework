from turtle import *

k = 100
tracer(0)
left(90)
pendown()
begin_fill()
rt(315)
for i in range(2):
    fd(16*k)
    rt(45)
    fd(8*k)
    rt(135)
end_fill()
penup()
canvas = getcanvas()
count = 0
for x in range(-300, 300):
    for y in range(-300, 300):
        if (canvas.find_overlapping(x * k, y * k, x * k, y * k)) == (5,):
            count += 1

print(count)
done()
#77