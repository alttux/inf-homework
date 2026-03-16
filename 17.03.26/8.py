alph15 = '0123456789abcde'
alph13 = '0123456789abc'

min_A = float('inf')
for x in range(13):
    for y in range(13):
        M_str = '2' + alph15[y] + '23' + alph15[x] + '5'
        M = int(M_str, 15)
        N_str = '67' + alph13[x] + '9' + alph13[y]
        N = int(N_str, 13)
        if N == 0:
            continue
        rem = M % N
        A = (N - rem) % N
        if A == 0:
            A = N
        if A < min_A:
            min_A = A
print(min_A)
