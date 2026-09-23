f = open('task3.txt')
n = f.readline()
data = sorted([list(map(int, s.split())) for s in f.readlines()])
out = []
for i in range(len(data)-1):
    if data[i][0] == data[i+1][0]:
        # print(data[i][0], data[i+1][1]-data[i][1]-1)
        out.append([data[i+1][1]-data[i][1]-1, data[i][0]])

print(max(out)[1], max(out)[0])
