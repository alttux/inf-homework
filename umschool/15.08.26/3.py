f = open('3.txt')
data = [int(l) for l in f]
temps = []
for x in range(len(data)-1):
    temps.append(((data[x+1]-data[x])/data[x])*100)

sr_temp = sum(temps)/len(temps)
print(sum(map(lambda i: ((data[i+1]-data[i])/data[i])*100 > sr_temp, range(len(data)-1))))