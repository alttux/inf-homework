lst = [1, 2, 3, 4, 5, 6]
lst[1::2] = lst[1::2][::-1]
print(lst)
