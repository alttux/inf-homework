for n in range(100, 1000):
    n1, n2, n3 = str(n)
    # print(n1, n2, n3)
    nb1 = int(n1)**2 + int(n2)**2
    nb2 = int(n2)**2 + int(n3)**2
    nb = str(max(nb1, nb2))+str(min(nb1, nb2))
    r = int(nb)
    if r == 5834:
        print(n, r)