from math import dist

f = open('2.txt')
f.readline()

data = [list(map(float, line.replace(',', '.').strip().split())) for line in f.readlines()]
# print(data)

clusters = [[], [], []]
for x, y in data:
    if x < 2:
        clusters[0].append([x, y])
    elif y < 5.5:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])

# print(clusters)
centre_points = [[], [], []]
for i in range(len(clusters)):
    cluster = clusters[i]
    min_sum_dist = 10 ** 10
    for point in cluster:
        sum_dist = 0
        for p2 in cluster:
            distance = dist(point, p2)
            sum_dist += distance
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            centre_points[i] = point

# print(centre_points)

Px = sum([x for x, y in centre_points]) / len(centre_points)
Py = sum([y for x, y in centre_points]) / len(centre_points)

print(Px * 10_000, Py * 10_000)
