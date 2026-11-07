for x in '0123456789ABCDEF':
    n1 = f'D49{x}1'
    n2 = f'48A3{x}'
    n = int(n1, 16) + int(n2, 16)
    if n % 14 == 0:
        print(n//14)