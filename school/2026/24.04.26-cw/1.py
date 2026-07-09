def DEL(n, m):
    return n%m==0

for A in range(1, 1000):
    c = 0
    for x in range(1, 1000):
        # if (not(x%100==0) and (x%4==0)) or (x%400==0) or (not(x%A==0)):
        if (not (DEL(x, 100)) and (DEL(x, 4))) or (DEL(x, 400)) or (not(DEL(x, A))):
            c+=1
    if c == 999:
        print(A)
        break