from turtle import *
screensize(2000, 2000)
k = 15
# tracer(0)
left(90)

for _ in range(3):
    forward(26*k)
    right(90)
    forward(18*k)
    right(90)

penup()

forward(5*k)
right(90)
forward(7*k)
left(90)

pendown()

for _ in range(4):
    forward(64*k)
    right(90)
    forward(47*k)
    right(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(1, 'red')

# canvas = getcanvas()
# c = 0
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
#             c+=1
# print(c)

done()