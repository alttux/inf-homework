numbers = [7, 2, 9, 4, 1, 6]
smallest = min(numbers)
largest = max(numbers)
small_index = numbers.index(smallest)
large_index = numbers.index(largest)
numbers[small_index] = largest
numbers[large_index] = smallest
print(numbers)
