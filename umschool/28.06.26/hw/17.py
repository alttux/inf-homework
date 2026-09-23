nums = []
for x in range(2, 37):
    s = 49 * 52**32 + 33**123 + 74 * 43**121 - 751235
    c = 0
    while s > 0:
        if s % x == 4:
            c += 1
        s //= x

    nums.append([c, x])
    print(c, x)

print(max(nums))