f = open('task1.txt')
n = f.readline()
data = sorted([list(map(int, s.split())) for s in f.readlines()])
out = []
for i in range(len(data)-1):
    if data[i][0] == data[i+1][0] and \
        data[i+1][1] - data[i][1] == 3:
        out.append([data[i][0], data[i][1]+1])
print(out[-20:])
# 20164 104