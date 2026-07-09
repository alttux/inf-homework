from turtle import *

k = 50
num = 23
screensize(8000, 8000)
speed(1000)

begin_fill()
left(90)
pendown()


for i in range(4):
    fd(num * k)
    rt(90)
    fd(7 * k)
end_fill()
penup()

canvas = getcanvas()
count = 0
for x in range(-100, 1000):
    for y in range(-100, 1000):
        # print(canvas.find_overlapping(x * k, y * k, x * k, y * k))
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
            # print(canvas.find_overlapping(x * k, y * k, x * k, y * k))
            count += 1
print(count)
done()

#23