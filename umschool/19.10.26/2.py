f = open('task2.txt')
s = f.readline()
c = 100
s = s.replace('M',' ')

data = s.split(' ')
res = []
print(data)
for i in range(len(data)):
    res.append(len(''.join(data[i:i+c+1]))+c)
    print(data[i:i+c+1])

print(max(res))