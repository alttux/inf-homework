for A in range(300):
    ok = True
    for x in range(100):
        for y in range(100):
            if not ((not (x <= 9) or x*x <= A) and (not (y*y <= A) or y <= 9)):
                ok = False
                break
        if not ok:
            break
    if ok:
        best = A
print(best)   # 99