for g in range(1, 1001):
    if all( ( ((72%x==0) <= ((90%x!=0))) or ((g-x>80)) ) for x in range(1, 1001)):
        print(g)
        break