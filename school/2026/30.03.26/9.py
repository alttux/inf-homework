with open("9.txt") as f:
    for n, line in enumerate(f, 1):
        nums = list(map(int, line.split()))
        if len(set(nums)) == len(nums):
            if max(nums) - min(nums) == sum(nums) - max(nums) - min(nums):
                print(line, n)
                break