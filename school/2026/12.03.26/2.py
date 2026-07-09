for n in range(1000, 10000):
    p = n
    q = int(str(n)[::-1])
    if 4*p**2+4*p+1 == 1*q**2+4*q+4:
        print(p)
        break
# 3997