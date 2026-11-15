f = open('16.txt')
cnt = 0

for line in f:

    s = sorted(map(int, line.split()))

    cnt += 1

    repeat, not_repeat = [x for x in s if s.count(x) == 3], [x for x in s if s.count(x) == 1]

    if len(repeat) == 3 and len(not_repeat) == 4 and sum(not_repeat) > sum(repeat):

        print(cnt)