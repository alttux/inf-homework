f = open('task.txt')
# map() на каждую строку для преобразования типов
f = open('task.txt')

# Задание с символьными данными: подсчёт пар символов
l = f.readline()
ltrs = {}.fromkeys(set(l), 0)  # словарь с нулями для каждого уникального символа

for i in range(len(l) - 1):
    l1, l2 = l[i: i + 2]
    # Условие: следующий символ — 'Z'
    if l2 == 'Z':
        ltrs[l1] += 1

print(ltrs)
# Сортировка по значению (по возрастанию количества)
print(sorted(ltrs, key=ltrs.get))
