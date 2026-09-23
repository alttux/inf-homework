f = open('task.txt')
words = {}
line = f.readline().split()
for word in line:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# Слово, встречающееся чаще всего
print(max(words, key=words.get))
