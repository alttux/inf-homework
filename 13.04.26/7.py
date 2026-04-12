for g in range(1, 1001):
    if all(( ((x%g!=0)) <= ((x%6==0) <= ((x%9!=0))) ) for x in range(1, 1001)):
        print(g)