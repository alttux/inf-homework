def F(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    if n % 2 == 0:
        res = 11 * n + F(n - 1)
    else:
        res = 11 * F(n - 2) + n
    memo[n] = res
    return res

total = sum(F(n) for n in range(35, 51) if F(n) % 2 == 0)
print(len(str(total)))  # 25