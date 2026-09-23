numbers = [1, 2, 3, 4, 5, 6]
odd = numbers[1::2]
odd.reverse()
numbers[1::2] = odd
print(numbers)
