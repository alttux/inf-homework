def i(s, e):
    if s == e:
        return 1
    elif s < e:
        return 0

    return i(s-1, e) + i(s//3, e)

print(i(33, 7) * i(7, 2))