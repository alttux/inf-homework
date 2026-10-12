for a in range(1, 1000):
    for x in range(1, 1000):
        if ((x & 17 == 0) <= ((x & 37 == 0) or (x & a != 0))) == False:
            break

    else:
        print(a)
        break