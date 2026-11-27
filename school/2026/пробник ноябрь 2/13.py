def task(s, e):
    if s < e or s == 38:
        return 0
    elif s == e:
        return 1
    return task(s-2, e) + task(s-6, e) + task(s//2, e)

print(task(70, 19)*task(19,8))
