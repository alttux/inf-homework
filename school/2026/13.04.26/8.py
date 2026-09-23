for g in range(1, 1001):
    if all( ( (120%g==0) and ((x%g!=0) <= ((x%18==0) <= ((x%24!=0)))) ) for x in range(1, 1001)):
        print(g)