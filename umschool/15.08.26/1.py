f = open('1.txt')
data = [int(l) for l in f]
print(sum(map(lambda i: data[i] < data[i+1], range(len(data)-1))))