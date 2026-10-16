def functional(n: int) -> bool:
    res = 0
    for i in str(n):
        res += int(i)**len(str(n))

    return res == len(str(n))
#
# f = open('4.txt')
# s = f.readline()
#
# for i in range(len(s)-4):
#     nums = []
#     for j in range(5):
#         nums.append(s[i+j])
#     num = ''.join(nums)
#     print(num)
for p in range(100000):
    if functional(p) == True:
        print(p)