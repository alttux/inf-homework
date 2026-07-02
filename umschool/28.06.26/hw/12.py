from string import digits, ascii_uppercase
s = 3 * 5103**2020 + 3 * 729**2021 - 2 * 343**2022 + 27**2023 - 4 * 7**2024 - 2029
alph = digits + ascii_uppercase
c = 0
while s > 0:
    if s % 36 > 12:
        c += 1
    s //= 36

print(c)