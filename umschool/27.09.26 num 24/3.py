s = open('24.3.txt').readline().replace('O', ' ').split(' ')
ass= []
for i in range(len(s)-1):
    ass.append(len(s[i+1])+len(s[i])+1)

print(max(ass))