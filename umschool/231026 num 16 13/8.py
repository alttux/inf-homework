def t13(start, end):
    if start > end or start == 12:
        return 0
    elif start == end:
        return 1
    return t13(start+1, end) + t13(start*2, end) + t13(start**2, end)

print(t13(5, 48))