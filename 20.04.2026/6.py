for G in range(1, 1000):
    if all(
            (f < G) or (h < G) or (h < f - 5) or (h < 2 * f - 15)
            for h in range(0, 100)
            for f in range(0, 100)
    ):
        print(G)
        break
