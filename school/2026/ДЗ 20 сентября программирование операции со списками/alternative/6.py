numbers = [1, 2, 2, 3, 4, 4, 4]
unique = []
for value in numbers:
    if value not in unique:
        unique.append(value)
print(len(unique))
