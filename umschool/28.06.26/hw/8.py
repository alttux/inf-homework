from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:9]
for x in alph:
    s1 = f'55{x}36'
    s2 = f'{x}2524'
    s = int(s1, 19) + int(s2, 19)
    if s % 11 == 0:
        print(s//11)
        break
