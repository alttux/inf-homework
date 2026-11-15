from math import  dist


f = open('27_1.txt')
f.readline()
data = [list(map(float, l.replace(',', '.').split())) for l in f.readlines()]

clusters = [[] for _ in range(3)]
for x, y in data:
    if y < 0:
        clusters[0].append([x, y])
    elif x > 2:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])

good_dots = [[] for _ in range(3)]
# print(good_dots)
for i in range(len(clusters)):
    min_dist =10000000000
    for c1 in clusters[i]:
        sum_dist = 0
        for c2 in clusters[i]:
            sum_dist += dist(c1, c2)
        if sum_dist < min_dist:
            min_dist = sum_dist
            good_dots[i] = c1

# print(good_dots)
#
Px = sum([x for x, y in good_dots])/3
Py = sum([y for x, y in good_dots])/3
#
print(Px*10_000, Py*10_000)



