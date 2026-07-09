for A in range(93, 4, -1):
    k = 0
    for x in range(1, 1000):
        if not(((x&46 != 0) <= ((x&A != 0) <= (x&70 != 0))) <= ((x&6==0) and (x&A!=0) and (x&70==0))):
            k+=1
    if k == 999:
        print(A)
        break