file = open('files/17_03.txt')
nums = [int(line) for line in file]
mean_of_odds = sum([x for x in nums if x %2==1])/len([x for x in nums if x %2==1])
out = []
for num1, num2 in zip(nums, nums[1:]):
    if (num1%7==0 and num2%7!=0 and num2>mean_of_odds) or (num2%7==0 and num1%7!=0 and num1>mean_of_odds):
        out.append(num1+num2)

print(len(out), min(out))