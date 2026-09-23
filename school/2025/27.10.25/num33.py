from turtle import*
k = 25
speed(100000)
tracer(0)
screensize(2000, 2000)
lt(90)
c=0
begin_fill()
for i in range(2):
    fd(5*k)
    rt(90)
    fd(10*k)
    rt(90)
end_fill()
pu()
cv = getcanvas()
for x in range(-500, 500):
    for y in range(-500, 500):
        if cv.find_overlapping(x*k, y*k, x*k, y*k) != ():
            c+=1
print(c)
done()
#66