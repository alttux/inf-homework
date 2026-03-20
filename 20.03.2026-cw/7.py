alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


for x in range(0,10):
    n1 = f'{x}a04'
    n2 = f'1d{x}3'
    a = int(n1, 13) + int(n2, 18)
    if a%184==0:
        print(x, a, a//184)
        # 124