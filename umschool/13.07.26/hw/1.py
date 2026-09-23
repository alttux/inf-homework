def del_7(x):
    return (int(x)%7)**2

f = open('a5404cba-0e50-4fd9-91b3-063f231c8133_test.txt','r')
l = f.readlines()
s = l[0].split()
print(sum(list(map(del_7, s))))