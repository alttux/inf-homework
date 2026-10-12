a = list(map(int, open('17.txt').read().split()))
f = lambda x: 1000 <= abs(x) <= 9999
m = max(x for x in a if f(x) and abs(x) % 100 == 43) ** 2
r = [(a[i] + a[i + 1]) ** 2 for i in range(len(a) - 1) if (f(a[i]) or f(a[i + 1])) and (a[i] + a[i + 1]) ** 2 < m]
print(len(r), max(r))