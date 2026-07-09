alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnmйцукенгшщзфывапролдячсмить')

def to_10(n,a):
    result = 0
    for i, char in enumerate(reversed(n)):
        val = alph.index(char)
        result += val * (a ** i)
    return result

for x in alph[:48]:
    n1 = f'1{x}24a'
    n2 = f'{x}2024'
    n3 = f'6{x}08'
    a = to_10(n1,47) + to_10(n2,47) - to_10(n3,47)
    if a%46==0:
        print(x, to_10(x, 47), a, a//46)
# 178814420