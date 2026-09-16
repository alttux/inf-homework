f = open('task.txt')
data = [int(x) for x in f]

# map() применяет функцию к каждому элементу
# Подсчёт количества возрастаний в последовательности
print(sum(map(lambda i: data[i] < data[i + 1], range(len(data) - 1))))
