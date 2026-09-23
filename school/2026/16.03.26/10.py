alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
lst = []

for q in range(11, 36):
    n1 = f'913a2125'
    n2 = f'71236911'
    a = int(n1, q) + int(n2, q)
    if a%22==0:
        print(q, a/22)
# 77494892