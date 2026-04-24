for A in range(1, 1000):
    if all(
            (not ((x | 41 == 0) or (x & 128 != 0))) and (x & A == 0) and ((x | A == 0) or (x & A == 0))
            for x in range(10, 100)
    ):
        print(A)
        break
