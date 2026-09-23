def DEL(x, a):
    if x%a==0:
        return True
    else:
        return False

def f(x, a):
    r = (not(DEL(x, a))) <= (((not((DEL(x, 48))) or (not(DEL(x, 35))))))
    return r

for A in range(1, 5000):
    if all(f(x, A) for x in range(1, 5001)):
        print(A)

