for x in '0123456789ABCDEFGHI':
    n1 = f'85{x}6127'
    n2 = f'3{x}749'
    n3 = f'62{x}3'
    n = int(n1, 19) + int(n2, 19) + int(n3, 19)
    if n % 18 == 0:
        print(n/18, n, x)