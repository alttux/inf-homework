from string import digits, ascii_uppercase
for x in sorted(digits+ascii_uppercase)[:21]:
    n1 = f'33{x}7'
    n2 = f'124{x}{x}855'
    n = int(n1, 21) + int(n2, 21)
    if n%20==0:
        print(n//20)
