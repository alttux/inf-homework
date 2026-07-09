alph = '0123456789abcdefghijk'

def to_10(n, a):
    result = 0
    for i, char in enumerate(reversed(n)):
        val = alph.index(char)
        result += val * (a ** i)
    return result

for x in range(21):
    for y in range(21):
        num1 = to_10('12' + alph[y] + alph[x] + '9', 21)
        num2 = to_10('36' + alph[y] + '99', 21)
        if (num1 + num2) % 18 == 0:
            y = 5
            num1 = to_10('12' + alph[y] + alph[x] + '9', 21)
            num2 = to_10('36' + alph[y] + '99', 21)
            result = (num1 + num2) // 18
            print(result)
            break