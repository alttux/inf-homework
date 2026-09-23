def sqr(x):
    return int(x) ** 2


f = open('map1.txt')
for line in f:
    print(sum(list(map(sqr, line.split()))))