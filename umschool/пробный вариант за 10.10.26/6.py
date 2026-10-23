from turtle import *
k = 10
tracer(0)
speed(1)
screensize(2000, 2000)

print(20 * 27 + 7 * 27 + 13 * 14 + 4 + 4)

left(90)

for _ in range(2):
    forward(17*k)
    right(90)
    forward(23*k)
    right(90)

    penup()

    forward(5*k)
    right(90)
    forward(11*k)
    left(90)

    pendown()

    for _ in range(2):
        forward(26*k)
        right(90)
        forward(19*k)
        right(90)


penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*k, y*k)
        dot(1,'red')

done()

