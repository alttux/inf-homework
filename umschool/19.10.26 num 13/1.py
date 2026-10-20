def calc(start,end):
    if start > end:
        return 0
    if start == end:
        return 1
    return calc(start+1, end) + calc(start*2, end)

print(calc(1, 16))