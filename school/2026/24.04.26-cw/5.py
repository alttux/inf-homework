for B in range(0, 1000):
    if all(
            ((x & 500 != 0) and (x & 200 == 0)) <= (not (x & B == 0))
            for x in range(0, 1000)
    ):
        print(B)
        break
