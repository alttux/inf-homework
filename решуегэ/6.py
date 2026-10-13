import turtle
k = 10

t = turtle.Turtle()
t.left(90)
turtle.tracer(0)
for _ in range(4):
    t.forward(10*k)
    t.right(90)

t.penup()
for x in range(-10, 15):
    for y in range(-10, 10):
        t.setpos(x*k, y*k)
        t.dot(2)

turtle.done()