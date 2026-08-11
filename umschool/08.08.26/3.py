f = open('task3.txt')
conf = {}
for l in f:
    param = l.strip().split(' = ')
    if int(param[1]) < 50:
        conf[param[0]] = int(param[1])*2
    elif int(param[1]) > 200:
        conf[param[0]] = int(param[1]) / 2

print(sorted(conf, key=conf.get)[:3])

