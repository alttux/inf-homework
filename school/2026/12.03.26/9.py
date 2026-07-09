for p in range(7, 20):
    for y in range(1, p):
        for x in range(1, p):
            for z in range(0, p):
                num1 = y * p**2 + 4 * p + y
                num2 = y * p**2 + 6 * p + 5
                result = x * p**3 + z * p**2 + 3 * p + 3
                if num1 + num2 == result:
                    xyz_decimal = x * p**2 + y * p + z
print(xyz_decimal)
