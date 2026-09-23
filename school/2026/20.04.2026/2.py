for G in range(1001, 0, -1):
    if all(
            (f>=G) or (h>=G) or (f*h<=205)
        for f in range(1, 101)
        for h in range(1, 101)
    ):
        print(G)
        break