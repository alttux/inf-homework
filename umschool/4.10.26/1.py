s = open('24.1.txt').readline()
cur_len = 0
max_len = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 0
print(max_len+1)