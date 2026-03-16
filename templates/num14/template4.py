alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnmйцукенгшщзфывапролдячсмить')

def to_10(n,a):
    result = 0
    for i, char in enumerate(reversed(n)):
        val = alph.index(char)
        result += val * (a ** i)
    return result
