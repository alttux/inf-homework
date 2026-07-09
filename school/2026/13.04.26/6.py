for g in range(1, 1001):
    if all( ( (g < 50) and ((x%g!=0)  <= ((x%10==0) <= (x%12!=0))) ) for x in range(1, 1001)):
        print(g)
