def i(s, e):
    if s > e or s == 19:
        return 0
    elif s == e:
        return 1
    return i(s+1, e) + i(s*2, e)

print(i(2, 10) * i(10, 29))

# print(i(1, 3))
