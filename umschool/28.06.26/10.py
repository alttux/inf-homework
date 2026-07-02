alph = '0123456789ABCDE'
for x in alph:
    s1 = f'97968{x}15'
    s2 = f'7{x}233'
    s = int(s1, 15) + int(s2, 15)
    if s % 14 == 0:
        print(x, s//14)
        break

# 116071912
