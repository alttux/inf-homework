from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:8]

for x in alph:
    s1 = f'AB5{x}3'
    s2 = f'EF{x}13'
    s = int(s1, 18) + int(s2, 18)
    if s % 17 == 0:
        print(s//17)
        break
