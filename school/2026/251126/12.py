from itertools import product


c = 0
for n in product('123456', repeat=4):
    n = ''.join(n)
    if n.count('4') == 1 and len([x for x in n if int(x) % 2 == 0]) <= len([x for x in n if int(x) % 2 != 0]):
        c+=1


print(c)