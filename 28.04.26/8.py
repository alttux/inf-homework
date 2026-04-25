count = 0
for d0 in range(1, 15):
    for d1 in range(0, 15):
        if d1 == d0: continue
        for d2 in range(0, 15):
            if d2 == d1: continue
            for d3 in range(0, 15):
                if d3 == d2: continue
                digits = [d0, d1, d2, d3]
                if digits.count(8) == 1:
                    count += 1
print(count)