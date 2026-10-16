for x in range(24):
    if all( (8 * 24**0 + x * 24**1 + 4 * 24**2 + 1 * 24**3 + y * 24**4 + 2 * 24**5) % 16 == 0 for y in range(24)):
        print(x, 3 * 24**0 + x * 24**1) # x3 - не влияет на ответ
        #23 | 0123456789ABCDEFGHIJKLM N

res = int('DN1', 30)
res3 = ''
while res > 0:
    res3 = str(res%3) + res3
    res//=3

print(res3)

