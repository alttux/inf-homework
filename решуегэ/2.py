def F(x, y, z, w):
    return int((x == (w or y)) or ((not w or z) and (not y or w)))

print("x y z w | F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(F(x, y, z, w)):
                    print(x, y, z, w, "|", F(x, y, z, w))