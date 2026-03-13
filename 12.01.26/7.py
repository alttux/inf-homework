alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')

def to_a(x, a):
    s = ''
    while x > 0:
        s = alph[x % a] + s
        x//=a
    return s

for n in range(2, 36):
    if len(to_a(70, n)) == 3:
        print(n)
        break

# 5