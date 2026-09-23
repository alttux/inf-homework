f = open('task4.txt')
items = {}
for l in f:
    item = l.strip().split(': ')
    if int(item[1]) > 10:
        items[item[0]] = int(item[1])
        if int(item[1]) > 100:
            items[item[0]] = int(item[1])*0.8
print(int(sum(items.values())))