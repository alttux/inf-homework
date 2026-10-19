f = open('17.txt')
data = [int(x) for x in f.readlines()]
c = 0
for i in range(len(data)-2):
    n1 = data[i]
    n2 = data[i+1]
    n3 = data[i+2]
    good = []
    for n in (n1, n2, n3):
        if str(n)[-1] == '6' and len(str(abs(n))) == 4:
            good.append(n)
    if len(good) == 2 and sum([n1, n2, n3]) < max(good):
        print(n1, n2, n3)
        c+=1

print(c)