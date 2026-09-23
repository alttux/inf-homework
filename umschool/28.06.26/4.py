s = 32**2023 + 16**2022 - 256**101
nums = []
while s > 0:
    nums.append(s%18)
    s //= 18
print(len(set(nums)))

# 18