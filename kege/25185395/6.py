from turtle import *

k = 1.5
perim = 0
tracer(0)
left(90)

def fwd(n):
    global perim
    forward(n * k)
    perim += n

# Повтори 2 [Повтори 2 [Вперёд 190 Направо 120] Направо 120]
for _ in range(2):
    for _ in range(2):
        fwd(190)
        right(120)
    right(120)

# Направо 150 Вперёд 13 Направо 90 Вперёд 380 Направо 90 Вперёд 13
right(150); fwd(13)
right(90);  fwd(380)
right(90);  fwd(13)

# Направо 30 Вперёд 67  — перерисовывает часть отрезка 1, не входит в периметр
right(30)
color('red')
fwd(67)
color('black')
perim -= 67  # не часть контура

write(f'Периметр = {perim}', font=('Arial', 14, 'bold'))

update()
done()
