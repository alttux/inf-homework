def mdist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


f = open('2.txt')
f.readline()

data = [list(map(float, p.replace(',', '.').split())) for p in f]

clusters = [[] for _ in range(3)]
for x, y in data:
    if x < 2: clusters[0].append([x, y])
    elif y < 3: clusters[1].append([x, y])
    else: clusters[2].append([x, y])

centroids = [[] for _ in range(3)]
for i in range(len(clusters)):
    min_sum_dist = 10**10
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += mdist(p1, p2)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            centroids[i] = p1

px = sum(x for x,y in centroids) / len(centroids)
py = sum(y for x,y in centroids) / len(centroids)
print(int(px * 10_000 // 1), int(py * 10_000 // 1))
