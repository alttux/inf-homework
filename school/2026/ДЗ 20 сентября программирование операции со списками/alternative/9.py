numbers = [1, 2, 2, 3, 3, 3, 4]
pairs = 0
for value in set(numbers):
    amount = numbers.count(value)
    pairs += amount * (amount - 1) // 2
print(pairs)
