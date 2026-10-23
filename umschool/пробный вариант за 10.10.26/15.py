for a in range(0, 1000):
    if all(((x + y <= 45) or (y <= 3*x - 7) or (y >= a)) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)