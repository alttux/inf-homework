def i(s, e):
    if s == e:
        return 1
    elif s > e:
        return 0
    return i(s+2, e) + i(s*2, e) + i(s*2+1, e)

print(i(1, 24))