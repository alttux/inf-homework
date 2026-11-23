f = open('5.txt')
c = 0
for l in f:
    s = list(map(int, l.split()))
    d = [1] * len(s) # список для длин подпоследовательностей
    for i in range(len(s)):
        for j in range(i):
            if s[j] > s[i]: # если числа убывают
                d[i] = max(d[i], d[j] + 1)

    bp = [x for x in s if s.count(x) > 2]   # для условия - в строке все числа встречаются не более двух раз;
    if max(d) > 2 and bp == [] and len(set(s)) == 5:
        c+=1

print(c)
