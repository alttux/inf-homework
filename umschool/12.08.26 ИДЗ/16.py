from string import digits, ascii_uppercase
for x in sorted(digits+ascii_uppercase)[:20]:
    n1 = f'28AC7IH{x}F'
    n2 = f'15JDFBG27{x}4'
    n = int(n1, 20) + int(n2, 20)
    if n%769==0:
        print(hex(n//7))
