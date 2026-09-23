f = open('2.txt')
data = [int(x) for x in f]
data_first = data[:len(data)//2]
data_second = data[len(data)//2:]
median = lambda lst: sum(sorted(lst)[len(lst)//2-1:len(lst)//2+1])/2
print(abs(median(data_first)-median(data_second)))