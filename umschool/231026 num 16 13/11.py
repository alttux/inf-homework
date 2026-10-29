def task13(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        if str(start)[-2] == '9':
            return task13(start+2, end) + task13(start, end)
        return task13(start+1, end) + task13(start+10, end)

print(task13(11, 27))