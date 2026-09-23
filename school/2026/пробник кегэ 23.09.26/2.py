for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((w == (not x)) <= (not (z <= w))) or (not y)
                if not f:
                    print(x, w, y, z)