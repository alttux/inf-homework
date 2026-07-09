nums = [int(s) for s in open('files/17.9.2_kaLkXQu.txt')]
out = []
for i in range(len(nums)-1):
    n1 = nums[i]
    n2 = nums[i+1]
    if n1%2 == n2%2:
        out.append(n1+n2)
print(len(out), max(out))