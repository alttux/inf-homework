alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
lst = []
for x in alph[:25]:
    for y in alph[:25]:
        if int(f'7{y}23{x}5', 25) % 131 == 0:
            lst.append(int(f'7{y}23{x}5', 25)//131)
print(max(lst))