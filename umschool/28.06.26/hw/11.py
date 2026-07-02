from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:2]

for x in alph:
    s1 = f'32D{x}'
    s2 = f'43{x}B'
    s = int(s1, 16) + int(s2, 12)
    if s % 15 == 0:
        print(str(s)[0])