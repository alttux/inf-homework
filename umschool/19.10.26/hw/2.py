f = open('2.txt')
s = f.readline()
c = 150

s = s.replace('O', ' ')
res = []
data = s.split(' ')
for i in range(len(data)):
    res.append(len(''.join(data[i:i+c+1]))+c)

print(max(res))