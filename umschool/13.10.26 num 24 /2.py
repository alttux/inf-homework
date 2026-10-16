f = open('2.txt')
s = f.readline()
buffer = s[0]
good = []

for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isdigit():
        buffer += s[i+1]
    else:
        buffer = s[i+1]
    if buffer.isdigit():
        if all(x not in buffer for x in '02468'):
            good.append(int(buffer))


print(max(good))

