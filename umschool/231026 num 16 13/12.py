def task(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return task(s+1, e) + task(s*2, e) + task(s*3, e)

print(task(5, 19)*task(19,45) + task(5, 25)*task(25,45) - task(5, 19)*task(19, 25)*task(25, 45))