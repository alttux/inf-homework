for G in range(1, 300):
    if all(
            (f < 9) <= ((5 * h < f) <= (2 * f * h < G))
            for h in range(1, 300)
            for f in range(1, 300)
    ):
        print(G)
        break
