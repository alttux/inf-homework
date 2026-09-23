for p in range(2, 50):
    for z in range(1, p):
        for x in range(0, p):
            for y in range(0, p):
                for B in range(0, p):
                    k = (z * p + x) + (x * p + y)
                    n = z * p ** 2 + y * p + B
                    if k == n:
                        print(int(str(x)+str(y)+str(z), p))
                        exit()
#5