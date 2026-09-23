f = open('porno.txt')
c=0
for s in f:
    # print(s)
    pizda = []
    l = s.split('\t')
    for st in l:
        pizda.append(int(st))

    if max(pizda) < (sum(pizda) - max(pizda)):
        if pizda[0]+pizda[1] != pizda[2]+pizda[3] and pizda[0]+pizda[2] != pizda[1]+pizda[3] and pizda[0]+pizda[3] != pizda[1]+pizda[2]:
            c+=1


print(c)