from turtle import *

k = 20
count = 0
tracer(0)

left(90)

pendown()
begin_fill()
right(45)
for i in range(2):
    forward(5*k)
    right(45)
    forward(10*k)
    right(135)
end_fill()
penup()

canvas = getcanvas()

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
            count+=1

print(count) # 27
done()