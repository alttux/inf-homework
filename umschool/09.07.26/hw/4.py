file = open('files/17.10_AfuE9ly.txt')
nums = [int(line) for line in file]
max6x2 = max([abs(x) for x in nums if abs(x)%10==6])
out = []
for num1, num2 in zip(nums, nums[1:]):
    if (((num1%10==6) + (num2%10==6)) == 1 ) and (num1**2+num2**2) < max6x2**2:
        out.append(num1**2+num2**2)

print(len(out), max(out))
f = open("files/17.10_AfuE9ly.txt")

data = [int(x) for x in f]

res = []

max_6 = max([x for x in data if x % 10 == 6]) ** 2


for i in range(len(data) - 1):

    if ((data[i] % 10 == 6 and data[i + 1] % 10 != 6) or (data[i] % 10 != 6 and data[i + 1] % 10 == 6)) and \
        (data[i] ** 2 + data[i + 1] ** 2) < max_6:

        res.append(data[i] ** 2 + data[i + 1] ** 2)


print(len(res), max(res))

print(max6x2**2, max_6)