file = open('files/9614a93e-a9ea-4369-a9dc-5e4b80b51379_17_june.txt')
nums = [int(line) for line in file]
out = []
for num_before, num1, num2, num_after in  zip(nums, nums[1:], nums[2:], nums[3:]):
    if (((len(str(num1))==5) and (len(str(num2))==3)) or ((len(str(num1))==3) and (len(str(num2))==5))) and \
            (num_before%10!=9 and num_after%10!=9):
        out.append(num1+num2)

print(len(out), max(out))