f = open('task.txt')
n, k = map(int, f.readline().strip().split())
data = []

for s in f:
    p, h = map(int, s.split())
    # Ключ сортировки — отношение h/p (чем меньше, тем лучше)
    data.append([(h / p), p, h])

# Сортировка по возрастанию первого элемента (h/p)
data.sort()
print(data[:k], '|', data[k])

# Дополнительная сортировка выбранных по убыванию p
print(sorted(data[:k], key=lambda x: x[1], reverse=True))

# Сумма p среди выбранных
c = 0
for i in data[:k]:
    c += i[1]
print(c)
