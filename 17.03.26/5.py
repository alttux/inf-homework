alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnmйцукенгшщзфывапролдячсмить')

def to_10(n,a):
    result = 0
    for i, char in enumerate(reversed(n)):
        val = alph.index(char)
        result += val * (a ** i)
    return result

с = 0
for x in alph[:44]:
    if to_10(f'1{x}23', 44) % 3 == 0:
        с+=1

print(с)
