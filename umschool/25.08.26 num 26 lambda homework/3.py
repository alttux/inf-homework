f = open('3.txt')
n, k = map(int, f.readline().strip().split())
data = []
for s in f:
    p, h= map(int, s.split())
    data.append([(h/p), p, h])

data.sort()
print(data[:k], '|', data[k])

print(sorted(data[:k], key=lambda x: x[1], reverse=True))

c = 0
for i in data[:k]:
    c+=i[1]

print(c)