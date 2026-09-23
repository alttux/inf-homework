f = open('task2.txt')
n, m = map(int, f.readline().strip().split())
data = []
data_with_sert = []

for s in f:
    sert, k1, k2, *k34 = map(int, s.split())
    smma = k1+k2+max(k34)
    data.append(smma)
    data_with_sert.append([sert, smma])

data.sort(reverse=True)
data_with_sert.sort(reverse=True, key=lambda x: (x[0], x[1]))
print(data[:m], '|', data[m])
print(data_with_sert[:m], '|', data_with_sert[m])
# 223 240