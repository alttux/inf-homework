def deli(x, y):
    return x % y == 0

for a in range(1, 1000):
    if all((deli(x, a) and not(deli(x, 36))) <= (not deli(x, 12)) for x in range(1, 1000)):
        print(a)