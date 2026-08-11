from string import ascii_uppercase
name = "NIKITA"
alph = {letter: i for i, letter in enumerate(ascii_uppercase, 1)}

s = 0
for i in name:
    s+=alph[i]

print(s)