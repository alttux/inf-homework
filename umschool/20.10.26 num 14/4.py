for x in range(0, 9):
    n1 = f'{x}{x}34'
    n2 = f'{x}002'
    n = int(n1, 9)+int(n2, 9)
    if n % 8 == 0:
        print(n/8)