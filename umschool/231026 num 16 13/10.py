def task13(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        if int(str(s)[-2]) < int(str(s)[-1]):
            s2 = int(str(s)[:-2] + str(s)[-1] + str(s)[-2])
            return task13(s+1, e) + task13(s2, e)
        return task13(s + 1, e)


print(task13(160, 220))