f = open('task2.txt')
n = f.readline()
data = sorted([list(map(int, s.split())) for s in f.readlines()])

for i in range(len(data)-1):
    if data[i][0] == data[i+1][0] and \
        data[i+1][1] - data[i][1] == 6:
        print(data[i][0], data[i][1]+1)

# 8168 7604