print('a b c d F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((not(a) or b) == (not(c) or d) or (a and d)) == 0:
                    print(a, b, c, d, 0)
# cbad