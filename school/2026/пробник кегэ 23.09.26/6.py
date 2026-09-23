import turtle

k = 15
turtle.tracer(0)
t = turtle.Turtle()
t.setheading(90)

for i in range(5):
    t.forward(29 * k)
    t.right(90)
    t.forward(27 * k)
    t.right(90)

t.penup()
t.forward(3 * k)
t.right(90)
t.forward(9 * k)
t.left(90)
t.pendown()

for i in range(5):
    t.forward(72 * k)
    t.right(90)
    t.forward(95 * k)
    t.right(90)

t.penup()
c = 0
for x in range(0, 40):
    for y in range(0, 40):
        t.goto(x * k, y * k)
        if 9 <= x <= 27 and 3 <= y <= 29:
            t.dot(5, "red")
            c += 1
        else:
            t.dot(3, "black")

print(c)
turtle.update()
turtle.done()