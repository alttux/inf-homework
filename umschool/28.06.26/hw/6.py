s =  35**28 + 92**15 - 12**5
c = 0
while s > 0:
    if s % 5 == 3:
        c += 1
    s //= 5
print(c)
c_9 = ''
while c > 0:
    c_9 = str(c%9) + c_9
    c//=9

print(c_9)