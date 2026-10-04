s = open('4ee1cecc-9f2e-42d6-86ab-ccd877f8760a_24_4_дз.txt').readline().replace('ZXY', '*').replace('ZYX', '*')
for i in range(100):
    if '*'*i in s:
        print(i)