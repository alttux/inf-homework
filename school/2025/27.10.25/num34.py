from turtle import*
k = 50
speed(100000)
tracer(0)
screensize(2000, 2000)
lt(90)
c=0
begin_fill()
for i in range(12):
    rt(60)
    fd(2*k)
    rt(60)
    fd(2*k)
    rt(270)
end_fill()
pu()
cv = getcanvas()
for x in range(-500, 500):
    for y in range(-500, 500):
        if cv.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
            c+=1
print(c)
done()
#149