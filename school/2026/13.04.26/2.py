for G in range(1, 1000):
    if all( (G%45 == 0) and ((750%y == 0) <= ((G%y!=0) <= ((120%y!=0)))) for y in range(1, 1001)):
        print(G)
        break
