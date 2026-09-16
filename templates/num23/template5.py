from string import ascii_uppercase

name = 'Victoria'
# Словарь: буква -> номер по алфавиту (A=1, B=2, ...)
alph = {letter: i for i, letter in enumerate(ascii_uppercase, 1)}

s = 0
for i in name.upper():
    s += alph[i]

print(s)
