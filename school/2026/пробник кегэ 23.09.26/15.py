for a in range(1000, 0, -1):
    ok = True
    for x in range(1, 1000):
        f = (x % a == 0) or ((70 <= x <= 90) <= (x % 16 != 0))
        if not f:
            ok = False
            break
    if ok:
        print(a)
        break