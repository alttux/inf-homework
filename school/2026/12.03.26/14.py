def to_base(x, base):
    s = []

    while x > 0:
        s.append(x % base)
        x //= base

    return list(reversed(s))

a = 3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 * 125 ** 665 - 404

a_5 = to_base(abs(a), 5)

print(a_5.count(2))