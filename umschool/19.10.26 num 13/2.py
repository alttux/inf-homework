def num13(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1

    return num13(s+1, e) + num13(s*3, e)

print(num13(2,52))