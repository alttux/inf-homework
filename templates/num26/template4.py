f = open('task.txt')
n, m = map(int, f.readline().strip().split())
data = []

for s in f:
    tv, ma, ms = map(int, s.split())
    data.append([tv, ma, ms, sum([tv, ma, ms])])

# Сортировка: сначала по убыванию суммы, затем по убыванию ma, затем ms
data.sort(reverse=True, key=lambda x: (sum(x), x[1], x[2]))

print(data[:m])
print(data[m])
