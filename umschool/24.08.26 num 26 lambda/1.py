f = open('task1.txt')
n, s = map(int, f.readline().strip().split())
# print(n, s)
data = []

for l in f:
    tv, ma, ms = map(int, l.split())
    # print(type(tv))
    data.append([tv, ma, ms, sum([tv, ma, ms])])

data.sort(reverse=True, key=lambda x: (sum(x), x[1], x[2]))
print(data[:s])
print(data[s])

# 229 89