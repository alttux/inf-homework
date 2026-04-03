def DEL(x, a):
    if x%a==0:
        return True
    else:
        return False

def f(x, a):
    r = (DEL(x, 128)) <= ((not(DEL(x, a))) <= (not(DEL(x, 80))))
    return r

for A in range(1000, 1, -1):
    if all(f(x, A) for x in range(1, 1001)):
        print(A)
        break