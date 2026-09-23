f = open('2.txt', encoding="utf-8")
fruits = {}
for l in f:
    fruit = l.strip().split()
    if fruit[0] in fruits:
        fruits[fruit[0]]+=int(fruit[1])
    else:
        fruits[fruit[0]] = int(fruit[1])

print(sum(sorted(fruits.values())[-2:]))