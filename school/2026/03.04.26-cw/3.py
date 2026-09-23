def DEL(x, a):
    if x%a==0:
        return True
    else:
        return False

def f(x, y, a):
    r = (2*x - y >=a) and (y>=17) and (78 >= x)
    return r

for A in range(1, 1000):
    if all(not(f(x, y, A)) for x in range(1, 1001) for y in range(1, 1001)):
        print(A)
        break