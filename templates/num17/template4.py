file = open('task.txt')
nums = [int(line) for line in file]

# Предвычисляем: среднее чётных чисел
even = [n for n in nums if n % 2 == 0]
mean_of_even = sum(even) / len(even)

out = []
for num1, num2 in zip(nums, nums[1:]):
    # Ровно один из двух делится на 5, и хотя бы один меньше среднего чётных
    if ((num1 % 5 == 0) + (num2 % 5 == 0) == 1) and \
            (num1 < mean_of_even or num2 < mean_of_even):
        out.append(num1 + num2)

print(len(out), max(out))
