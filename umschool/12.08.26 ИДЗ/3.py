def n_to_x(n, x):
    s = ''
    while n > 0:
        s  =str(n%x) + s
        n //= x
    return s

rl = []
for n in range(0, 1000000):
    nb = n_to_x(n, 7)
    if n % 5==0:
        nb = '4' + nb[1:] + '1'
    else:
        nb = nb.replace('3', '2') + '6'

    r = int(nb, 7)
    if r > 509:
        rl.append(r)

print(min(rl))