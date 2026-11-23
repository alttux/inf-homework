from math import dist


f = open('2.txt')
f.readline()
data = [list(map(float, s.replace(',', '.').split())) for s in f ]

clusters = [[], [], []]

for x, y in data:
    if x >= 1:
        clusters[0].append([x,y])
    elif y < -1:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])

centers = [[], [], []]
for cluster in range(len(clusters)):
    mim_sum_dist = 10**10
    for point1 in clusters[cluster]:
        sum_dist = 0
        for point2 in clusters[cluster]:
            sum_dist += dist(point1, point2)
        if sum_dist < mim_sum_dist:
            mim_sum_dist = sum_dist
            centers[cluster] = point1

Px = sum([center[0] for center in centers])/ 3
Py = sum([center[1] for center in centers])/ 3
print(Px*10000, Py*10000)

