def task13(start, end):
    if start < end:
        return 0
    elif start == end:
        return 1
    return task13(start-1, end) + task13(start//2, end) + task13(start//3, end)

print(task13(43, 10)*task13(10, 4))