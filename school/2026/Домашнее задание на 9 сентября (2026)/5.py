for n in range(101, 105):
    s = ''
    while n > 0:
        s =  str(n%3) + s
        n = n // 3

    nt = s

    if n % 3 == 0:
        suffix = nt[-2:] if len(nt) >= 2 else nt.rjust(2, '0')
        nt = nt + suffix
    else:
        summs = nt.count('1')+nt.count('2')
        sumsx3 = summs*3
        smstroi = ''
        while sumsx3 > 0:
            smstroi =  str(sumsx3 % 3) + smstroi
            sumsx3 = sumsx3 // 3
        nt = nt + smstroi

    r = int(nt, 3)
    print(r)
    # if 880 < r < 920:
    #     print(r)