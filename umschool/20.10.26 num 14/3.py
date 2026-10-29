n = 7**28 - 14**10 + 49
c = 0

while n > 0:
    if n % 7 == 6:
        c+=1
    n//=7

print(c)