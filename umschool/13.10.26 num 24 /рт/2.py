f = open('24_2.txt')
s = f.readline()
buffer = s[0]
good_nums = []

for i in range(len(s)-1):
    if (int(s[i]) + int(s[i+1])) >= 10:
        buffer += s[i+1]
    else:
        buffer = s[i+1]
    good_nums.append(buffer)

print(len(max(good_nums, key=len)))