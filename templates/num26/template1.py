f = open('task.txt')
# Считываем n, m из первой строки
n, m = map(int, f.readline().strip().split())
data = []

for s in f:
    ru, inf, mat = map(int, s.split())
    # Добавляем сумму как первый элемент — для автоматической сортировки
    data.append([sum([ru, inf, mat]), inf, mat])

# Сортируем по убыванию суммы (первый элемент списка)
data.sort(reverse=True)

# data[:m] — поступившие, data[m] — первый непоступивший
print(data[:m], '|', data[m])
