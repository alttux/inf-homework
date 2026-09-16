f = open('task.txt')
n = f.readline()
# Читаем данные: каждая строка — список чисел, сортируем все строки
data = sorted([list(map(int, s.split())) for s in f.readlines()])

out = []
for i in range(len(data) - 1):
    # Проверка: одинаковый первый элемент, разница вторых == 3
    if data[i][0] == data[i + 1][0] and \
            data[i + 1][1] - data[i][1] == 3:
        out.append([data[i][0], data[i][1] + 1])

# Последние 20 результатов
print(out[-20:])
