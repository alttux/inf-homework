from string import ascii_uppercase, digits

alph = digits + ascii_uppercase[:10]

for x in alph:
    s1 = f'13{x}CF'
    s2 = f'47GH{x}'
    s = int(s1, 20) + int(s2, 20)
    if s % 19 == 0:
        print(s//19)
        break