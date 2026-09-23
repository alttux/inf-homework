f = open('task.txt')
conf = {}
for l in f:
    param = l.strip().split(' = ')
    # Изменяем значения по условию при чтении
    if int(param[1]) < 50:
        conf[param[0]] = int(param[1]) * 2
    elif int(param[1]) > 200:
        conf[param[0]] = int(param[1]) / 2

# Три ключа с наименьшими значениями
print(sorted(conf, key=conf.get)[:3])
