f = open('4.txt')
s = f.readline()
s = s.replace('RO', ' ')
c = 358
data = s.split(' ')
res = []
for i in range(len(data)):
    # print(len(''.join(data[i:i+c-1]))+c*2)
    # print(''.join(data[i:i+c-1]))
    res.append(len(''.join(data[i:i+c+1]))+c*2+2)

print(min(res))