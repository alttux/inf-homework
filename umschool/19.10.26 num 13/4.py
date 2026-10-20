def i(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    if s == 30:
        return 0

    return i(s+1, e) + i(s*3, e)

print(i(3, 20) * i(20, 80))