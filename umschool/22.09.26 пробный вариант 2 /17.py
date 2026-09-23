f = open('17.txt')
c = 0
data = [int(x) for x in f]
print(data)
for i in range(len(data)-1):
    n1 = data[i]
    n2 = data[i+1]
    if n1 % 13 == 0 or n2 % 13 == 0:
        c+=1

print(c)