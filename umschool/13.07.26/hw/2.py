def sqr(x):
    return (int(x)**(0.5))*4


f=open('91c1373e-3c90-4690-bfca-35f4cdcb436d_test.txt')
l = f.readline().split()
print(sum(list(map(sqr, l))))
