from turtle import *

k = 100
num = 17
screensize(5000, 5000)
speed(1000)

begin_fill()
left(90)
pendown()


for i in range(4):
    fd(num * k)
    rt(90)
    fd(3 * k)

end_fill()
penup()

canvas = getcanvas()
count = 0
for x in range(-100, 1000):
    for y in range(-100, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
            count += 1
print(count)
done()

# 17