arr = [0] * 100
for i in range(63):
    if i == 0:
        arr[i] = 3
    elif i > 0 and i % 2 != 0:
        arr[i] = arr[i - 1] * 3 + 1
    elif i > 0 and i % 2 == 0:
        arr[i] = arr[i - 2] + 2 * arr[i - 1]
print(arr[60])
