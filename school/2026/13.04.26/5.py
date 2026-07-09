for g in range(1, 1001):
    if all( ( (70%g==0) and ((x%28==0) <= ((x%g!=0) <= (x%21!=0))) ) for x in range(1, 1001)):
        print(g)