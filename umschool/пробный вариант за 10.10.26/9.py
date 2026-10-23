f = open('9.txt')
c = 0
for l in f:
    s = list(map(int, l.split()))
    if len(s) - len(set(s)) == 1:
        povtor = 0
        for i in s:
            if s.count(i) > 1:
                povtor = i
        bez_povtor = set(s)
        bez_povtor.remove(povtor)
        if povtor**2 > (sorted(bez_povtor, reverse=True)[0] * sorted(bez_povtor, reverse=True)[1]) :
            # print(s)
            c+=1

print(c)
# a =  set([1, 3, 5, 6])
# a.remove(1)
# print(a)
#
# print(sorted(a, reverse=True))