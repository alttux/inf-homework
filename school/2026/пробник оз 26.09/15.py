for a in range(1000, 0, -1):
    if all((x % 6 == 0) <= (not (x % a != 0 and x % 9 == 0)) for x in range(1, 1000)):
        print(a)
        break