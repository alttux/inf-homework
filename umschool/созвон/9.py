q = list(range(1, 11)) + [12, 14]
p = [2,4,6,7,8,10,14]
a = list(range(1, 1000))

for x in range(1, 1000):
    if ( ((x in p) <= (x in a)) and ((x in a) <= (x in q)) ) == False:
        a.remove(x)

print(a)
print(sum(a))