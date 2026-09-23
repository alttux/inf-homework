for i in range(10_000_000, 100_000_000):
    if i%2027==0 and str(i)[0]=='1' and str(i)[2]=='0' and str(i)[-2:]=='27':
        print(i, i/2027)