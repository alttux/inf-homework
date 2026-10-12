for a in range(1000, 0, -1):
    if all((x % 25 != 0) or (x % a == 0) or (x % 60 != 0) for x in range(1, 10000)):
        print(a)
        break