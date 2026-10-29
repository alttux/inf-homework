for n in range(100, 1000):
    r1 = str(int(str(n)[0]) + int(str(n)[1]))
    r2 = str(int(str(n)[1]) + int(str(n)[2]))
    r = str(min(int(r1), int(r2))) + str(max(int(r1), int(r2)))
    # print(r)
    if r == '711':
        print(n)
