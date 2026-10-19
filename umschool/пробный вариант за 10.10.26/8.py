from itertools import product

for num, i  in enumerate(product(sorted('СТРУНА'), repeat=6), 1):
    i = ''.join(i)
    if num % 2 != 0 and i.count('С') == 0 and i.count("Т") == 0 and i.count('У') == 2 and i.count('Н') == 1:
        print(num, i)