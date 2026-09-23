file = open('task1.txt')
words = {}
line = file.readline().split()
for word in line:
    if word in words:
        words[word] += 1
    else:
        words[word]  = 1

print(max(words, key=words.get))