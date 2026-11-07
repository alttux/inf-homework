
def t13(s, e):
    if s < e or s == 5:
        return 0
    elif s == e:
        return 1
    return t13(s-2, e) + t13(s-4, e) + t13(s//3, e)

print(t13(34, 14) * t13(14, 2))