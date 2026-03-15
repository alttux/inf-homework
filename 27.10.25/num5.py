from turtle import *

k = 100
num = 15
screensize(2000, 2000)
speed(1000)

begin_fill()
left(90)
pendown()


for i in range(4):
    fd(num * k)
    rt(90)
    fd(num * k)
    lt(90)
    fd(num * k)
    rt(90)
end_fill()
penup()

canvas = getcanvas()
count = 0
for x in range(-100, 1000):
    for y in range(-100, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            count += 1
print(count)
done()

# подбором
# 15