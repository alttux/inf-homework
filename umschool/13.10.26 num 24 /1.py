from string import ascii_uppercase
f = open('1.txt')
s = f.readline()
bufer = s[0]

for symb in ascii_uppercase:
    s = s.replace(symb, ' ')

nums = s.split()
nums6 = []
for num in nums:
    if len(num) == 6 and num[0]!='0':
        nums6.append(int(num))

print(min(nums6))