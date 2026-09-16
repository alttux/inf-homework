f = open('task.txt')
n, m = map(int, f.readline().strip().split())
data = []
data_with_sert = []

for s in f:
    # Распаковка: первый элемент — сертификат, остальные — баллы
    sert, k1, k2, *k34 = map(int, s.split())
    # Сумма: k1 + k2 + максимальный из оставшихся
    smma = k1 + k2 + max(k34)
    data.append(smma)
    data_with_sert.append([sert, smma])

data.sort(reverse=True)
# Сортировка по двум ключам: сначала по сертификату, потом по сумме
data_with_sert.sort(reverse=True, key=lambda x: (x[0], x[1]))

print(data[:m], '|', data[m])
print(data_with_sert[:m], '|', data_with_sert[m])
