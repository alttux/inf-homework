from string import ascii_uppercase, digits
for x in sorted(digits+ascii_uppercase)[:23]:
    n1 = f'68{x}3613'
    n2 = f'945{x}56'
    n = int(n1, 23) + int(n2, 23)
    if n % 22==0:
        print(x, int(x, 23), n/22)

# print()