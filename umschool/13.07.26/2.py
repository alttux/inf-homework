def sqr(x):
    return int(x) ** 0.5


f = open('map2.txt')

for l in f:
    print(sum(list(map(sqr, l.split()))))