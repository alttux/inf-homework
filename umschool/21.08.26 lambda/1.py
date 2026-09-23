f = open('1.txt')
data = [int(x) for x in f]
middle = sum(data)/len(data)
o = (sum(map(lambda x: (x - middle)**2, data))/len(data))**0.5
print(o)