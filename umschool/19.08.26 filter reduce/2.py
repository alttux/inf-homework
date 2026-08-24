from functools import reduce
a = [2, 3, -7, 5, 9, -2, 6, -4, -5, 10]
proi = reduce(lambda  x, y: x*y, a)
summa = sum(a)
print(summa*proi)