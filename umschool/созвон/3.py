for a in range(1000, 0, -1):
    if all( ((x + y <= 70) or (y <= x + 8)) or (y > a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break