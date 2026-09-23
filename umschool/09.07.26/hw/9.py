file = open('files/9614a93e-a9ea-4369-a9dc-5e4b80b51379_17_june.txt')
nums = [int(line) for line in file]
out =[]
for num1, num2 in zip(nums, nums[1:]):
    if ((len(str(num1)))==(int(str(num1)[0]))) and ((len(str(num2)))==(int(str(num2)[0]))):
        out.append(num1+num2)

print(len(out), min(out))