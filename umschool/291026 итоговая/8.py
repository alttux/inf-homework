from zoneinfo import reset_tzpath


def t13(s, e):
    if s > e or s == 26:
        return 0
    elif s == e:
        return 1
    return t13(s+2, e) + t13(s*2, e)

print(t13(2, 14) * t13(14, 56))