for G in range(1000, 1, -1):
    if  all((90%G==0) and ((y%G!=0) <= ((y%15==0) <= (y%20!=0))) for y in range(1, 1001)):
        print(G)
        break
