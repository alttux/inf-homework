for A in range(-100, 100):
    if all(
            ((y + x) ** 2 > 1048) or ((x + 20 < A) and (40 - y < A))
            for x in range(1, 2000)
            for y in range(1, 2000)
    ):
        print(A)
        break
