def i(s, e):
    if s > e:
        return 0
    elif s == 5:
        return 0
    elif s == e:
        return 1
    return i(s+1, e) + i(s+4, e) + i(s*3, e)

print(i(1,15)*i(15,25))