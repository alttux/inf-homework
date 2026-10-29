for x in sorted('123456789ABCDEF'):
    n1 = f'{x}ABC'
    n2 = f'DEF{x}'
    n = int(n1, 16) + int(n2, 16)
    if n % 15 == 0:
        print(n/15, x)