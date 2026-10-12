def deli(x, y):
    return x % y == 0

for a in range(1, 10000):
    # flag = True
    for x in range(1, 1000):
        if (deli(x, a) <= (deli(x, 21) or deli(x, 35))) == 0:
            # flag = False
            break
    # if flag == True:
    #     print(a)
    #     break
    else:
        print(a)
        break