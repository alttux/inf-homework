f = open('task.txt')
data = [int(x) for x in f]

# Среднее арифметическое
middle = sum(data) / len(data)

# Среднеквадратическое отклонение через map и lambda
o = (sum(map(lambda x: (x - middle) ** 2, data)) / len(data)) ** 0.5
print(o)
