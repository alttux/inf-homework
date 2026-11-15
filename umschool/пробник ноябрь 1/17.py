
f = open('17.txt')
data = [int(l) for l in f]
md = min(data)
res = []
for i in range(len(data)-1):
    n1 = data[i]
    n2 = data[i+1]
    if (n1%47==md) +  (n2%47==md) == 1:
        res.append(sum([n1, n2]))

print(len(res), max(res))
