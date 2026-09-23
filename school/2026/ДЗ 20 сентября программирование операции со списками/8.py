lst = [1, 2, 2, 3, 3, 3, 4]
x = lst[0]
count = lst.count(x)
for y in lst:
    if lst.count(y) > count:
        x = y
        count = lst.count(y)
print(x)
