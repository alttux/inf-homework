f = open('4.txt')
n, m = map(int, f.readline().split())
# print(n, m, type(n))
data = [s for s in f.readlines()]
out = []
# print(data)
for i in range(len(data)- 1):
    if ('1' in data[i] and '2' in data[i] and '3' in data[i])==False:
        out.append([data[i].count('0'), i+1])
        print(i+1, data[i].count('0'))

print(min(out))

# 7