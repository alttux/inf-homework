f = open('task.txt')
n = f.readline()
data = sorted([list(map(int, s.split())) for s in f.readlines()])

out = []
for i in range(len(data) - 1):
    if data[i][0] == data[i + 1][0]:
        # Разница между соседними значениями второго поля минус 1
        out.append([data[i + 1][1] - data[i][1] - 1, data[i][0]])

# Пара с максимальной разницей: [разница, id]
print(max(out)[1], max(out)[0])
