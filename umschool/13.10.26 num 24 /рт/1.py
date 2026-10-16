f = open('24_1.txt')
s = f.readline()
buffer = s[0]
good_nums = []
for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isdigit():
        buffer+=s[i+1]
    else:
        buffer = s[i+1]
    if buffer.isdigit():
        if int(buffer)%2!=0:
            good_nums.append(int(buffer))
print(good_nums)
print(max(good_nums))