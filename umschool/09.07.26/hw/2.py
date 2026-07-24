file  = open('files/15b815f1-3b65-41a9-a616-bbe30f828e40_17.2.txt')
nums = [int(line) for line in file]
out = []
for num1, num2 in zip(nums, nums[1:]):
    if num1%3==num2%3==0:
        out.append(num1+num2)

print(len(out), max(out))