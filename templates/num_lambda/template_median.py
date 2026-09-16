f = open('task.txt')
data = [int(x) for x in f]

# Медиана через lambda-функцию
# Для чётного количества — среднее двух средних элементов
median = lambda lst: sum(sorted(lst)[len(lst) // 2 - 1:len(lst) // 2 + 1]) / 2

# Делим данные пополам
data_first = data[:len(data) // 2]
data_second = data[len(data) // 2:]

print(abs(median(data_first) - median(data_second)))
