for G in range(1000, 0, -1):
    if all(
            (h+2*f>G) or (f<13) or (h<44)
        for h in  range(0,100)
        for f in range(0,100)
    ):
        print(G)
        break