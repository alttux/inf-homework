s = open('24.txt').read().strip()
p = [i for i, c in enumerate(s) if c == 'Z']
print(min(p[i + 269] - p[i] + 1 for i in range(len(p) - 269)))