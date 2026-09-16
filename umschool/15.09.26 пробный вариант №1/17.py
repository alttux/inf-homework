f = open('17.txt')
c = 0
sums = []
data = list(map(int, f.readlines()))
mel = min(data)
for i in range(len(data)-1):
    n1= data[i]
    n2 = data[i+1]
    if n1%37 == mel or n2%37 == mel:
        c+=1
        print(n1, n2, '|', n1+n2)
        sums.append(n1+n2)

print(c, max(sums))

