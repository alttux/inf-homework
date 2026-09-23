from itertools import  product
nums = 0
for i in product('012345678', repeat=7):
    if i[0] != '0' and i.count('6') == 1:
        c = 0
        for x in '13579':
            c += i.count(x)
        if c == 2:
            print(i)
            nums+=1

print(nums)
