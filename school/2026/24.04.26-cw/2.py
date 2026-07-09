for A in range(1000, 0, -1):
    if all(
            (39 != y + 2 * x) or (A < x) or (A < y)
            for x in range(0, 1000)
            for y in range(0, 1000)
    ):
        print(A)
        break