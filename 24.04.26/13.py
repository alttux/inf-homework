for A in range(5000):
    if all(
        ((x & 29) != 0) <= (((x & 17) == 0) <= ((x & A)!= 0))
        for x in range(5000)
    ):
        print(A)
        break
#12