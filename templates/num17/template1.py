nums = [int(s) for s in open('task.txt')]
out = []
for i in range(len(nums) - 1):
    n1 = nums[i]
    n2 = nums[i + 1]
    # Условие на пару соседних элементов
    if n1 % 10 == 0 and n2 % 10 == 0:
        out.append(n1 + n2)

# ЕГЭ обычно просит: количество пар и максимальную/минимальную сумму
print(len(out), max(out))
