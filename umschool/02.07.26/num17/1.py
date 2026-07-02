f = open('files/17.1.txt')
nums = [int(l) for l in f]
cnt = 0
nums_sum = []
for i in range(len(nums)-1):
    n1 = nums[i]
    n2 = nums[i+1]
    if n1%11==0 and n2%11==0:
        cnt+=1
        nums_sum.append(n1+n2)
print(cnt, min(nums_sum))

