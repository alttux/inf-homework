from math import dist

f = open('3.txt')
f.readline()

data = [list(map(float, s.replace(',', '.').split())) for s in f]

clusters = [[] for _ in range(5)]
for x, y in data:
    if x < -3: clusters[0].append([x, y])
    elif y < 0 and -3 < x < 2: clusters[1].append([x, y])
    elif y < 1 and 3 < x < 8: clusters[2].append([x, y])
    elif 3 < y  < 8 and -2 < x < 4: clusters[3].append([x, y])
    elif y > 5 and x > 4: clusters[4].append([x, y])

centroids = [[] for _ in range(5)]
for i in range(len(clusters)):
    min_sum_dist = 10**10
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1, p2)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            centroids[i] = p1

px = sum(x for x, y in centroids) / len(centroids)
py = sum(y for x, y in centroids) / len(centroids)
print(int(px * 10_000 // 1), int(py * 10_000 // 1))


