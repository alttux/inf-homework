f = open('3.txt')
s = f.readline()
s = s.replace('XZ', ' ')
c = 29
data = s.split(' ')
res = []
for i in range(len(data)-c+1):
    # print(len(''.join(data[i:i+c-1]))+c*2)
    # print(''.join(data[i:i+c-1]))
    res.append(len(''.join(data[i:i+c-1]))+c*2)

print(min(res))