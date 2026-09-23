f = open('task.txt')
c = 0
for l in f:
    # Сортируем числа строки и проверяем условие (треугольное неравенство)
    s = sorted(list(map(int, l.split())))
    if s[2] < s[1] + s[0]:
        c += 1

print(c)
