import turtle

t3 = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
turtle.screensize(5000, 5000)
t1.speed(1000)
t2.speed(1000)

scale = 30
t2.color('red')
t2.goto(0, 8.1*scale)
t1.left(90)
t1.pendown()
t2.pendown()

for i in range(2):
    t1.fd(15*scale)
    t1.rt(90)
    t1.fd(8*scale)
    t1.rt(90)

    t2.fd(15*scale)
    t2.rt(90)
    t2.fd(8*scale)
    t2.rt(90)
t3.penup()
for x in range(15):
    for y in range(15):
        t3.setpos(x*scale, y*scale)
        t3.dot(2)


turtle.done()
# 56