s = open('24.3.txt').readline()
cur_len = 0
max_len = 0
for i in range(len(s) - 1):
    if s[i].isdigit() and s[i+1].isdigit() and int(s[i]) % 2 != int(s[i + 1]) % 2:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_len+1)