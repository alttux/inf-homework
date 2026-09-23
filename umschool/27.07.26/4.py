from string import ascii_uppercase
name = 'Victoria'
alph = {letter: i for i, letter in enumerate(ascii_uppercase, 1)}
print(alph)
s = 0
for i in name.upper():
    print(alph[i])
    s+=alph[i]

print('--------------')
print(s)