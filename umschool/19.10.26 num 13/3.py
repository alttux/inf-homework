def i(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1

    return i(s+2, e) + i(s*3, e) + i(s**2, e)
print(i(3, 77))