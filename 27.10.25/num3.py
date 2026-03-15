from turtle import *

k = 20
screensize(5000, 5000)
tracer(0)
left(90)
pendown()
begin_fill()
num = 18
for i in range(4):
    fd(num * k)
    rt(90)
    fd(num * k)
    lt(90)
    fd(num * k)
    rt(90)
end_fill()
penup()

# for x in range(-500, 500):
#     for y in range(-500, 500):
#         goto(x*k, y*k)
#         dot(2, 'red')

canvas = getcanvas()
count = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            count += 1
print(count)
done()

# подбором
# 18