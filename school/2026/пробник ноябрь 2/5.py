def troi(n):
    s = ''
    while n > 0:
        s = str(n%3) + s
        n //= 3
    return s

res = []
for n in range(1, 1000):
    nt = troi(n)
    if n % 3 == 0: nt = '2' + nt + '01'
    else: nt = nt + troi((n%3)*4)
    r = int(nt, 3)
    # print(n, r)
    if r > 300 and r % 2 != 0:
        res.append(r)

print(min(res))
# print(troi(8))