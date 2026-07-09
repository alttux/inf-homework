from sympy import isprime

memo = {}

def F(n):
    if n in memo:
        return memo[n]
    if n < 2:
        return 1
    if n % 3 == 0:
        res = 2 * F(n - 1) + F(n - 2)
    else:
        res = 3 * F(n - 2) + F(n - 1)
    memo[n] = res
    return res

count = 0
for n in range(1, 36):
    value = F(n)
    digit_sum = sum(int(d) for d in str(value))
    if isprime(digit_sum):
        count += 1

print(count)  # 1