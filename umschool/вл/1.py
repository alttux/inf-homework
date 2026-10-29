def to_b(n, b):
    s = ""
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s

def R(n): # алгоритм который в условии
    s = to_b(n, 7) # а
    t = "".join([str(6 - int(c)) for c in s]) # б
    t_int = int(t) # десятичное
    S = sum(int(c) for c in to_b(t_int, 5)) # в
    if S % 2 == 0: # чётная сумма
        d = (int(str(S)[0]) + int(str(S)[-1])) % 7
    else: # нечётная сумма
        d = S % 7
    u = (t + str(d)).replace("0", "")
    if u != '':
        return int(u, 7) # д

good_r, good_n = 0, 0
for n in range(1, 500_001): # перебор
    r = R(n) # алгоритм из условия используем
    if r != None and r > 28810 and r % 2 == 0: # условие которое требуется
        if good_r == 0 or r < good_r:
            good_r, good_n = r, n

print(good_r, good_n) # 29212 12633

res = good_r + good_n

print(to_b(res, 9)) # 63354
