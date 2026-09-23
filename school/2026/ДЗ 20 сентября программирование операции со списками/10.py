lst = [7, 2, 9, 4, 1, 6]
i = lst.index(min(lst))
j = lst.index(max(lst))
lst[i], lst[j] = lst[j], lst[i]
print(lst)
