n = 125 + 25**3 + 5**9
s = ''
while n:
    s = str(n % 5) + s
    n //= 5
print(s, s.count('0'))   # 1001001000 7