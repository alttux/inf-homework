for a in range(0, 1000):
    if all((y > 250) or (x > 75) or ((5*x - 3*y )< a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
