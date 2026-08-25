f = open('2.txt')
n, m = map(int, f.readline().strip().split())
data = []
for s in f:
    ru, inf, mat = map(int, s.split())
    data.append([sum([ru, inf, mat]), inf, mat])

data.sort(reverse=True)
print(data[:m], '|', data[m])