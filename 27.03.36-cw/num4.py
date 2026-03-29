print("A B C |         | F")
for a in range(2):
    for b in range(2):
        for c in range(2):
            f1 = not a
            f2 = not b
            f3 = b and c
            f4 = (not b) and c
            f5 = f1 or f3 or f4
            print(a, b, c, '|', int(f1), int(f2), int(f3), int(f4), '|', int(f5))