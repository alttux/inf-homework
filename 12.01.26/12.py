alph = sorted('0987654321qwertyuiopasdfghjklzxcvbnm')
m = 1

for x in alph[:12]:
    for y in alph[:18]:
        a = int(f'67{x}{x}3', 12) + int(f'2{x}9{x}', 14) + int(f'44{x}{x}3', 15) - int(f'2{x}{y}7', 18)

        if a == abs(a) and a % 77 == 0:
            m *= int(x, 36)
            m *= int(y, 36)
print(m)