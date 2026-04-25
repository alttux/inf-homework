for A in range(1000, 1, -1):
    if all(
            (y>A) or (152 != 2*y + 3*x) or (A<x)
        for x in range(1, 1000)
        for y in range(1, 1000)
    ):
        print(A)
        break

# 30