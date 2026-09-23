with open("9.txt") as f:
    count = 0
    for line in f:
        nums = list(map(int, line.split()))
        mn = min(nums)
        mx = max(nums)
        avg = (sum(nums) - mx) / 5

        c1 = nums.count(mn) == 1
        c2 = any(nums.count(x) > 1 for x in nums)
        c3 = mx > 3 * avg

        if c1 and c2 and c3:
            count += 1

print(count)