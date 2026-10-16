s = 1234**1234 * 2345**2345 + 57**5557 * 4321**4321
st = ''
alph = '0123456789ABCDEFGH'
while s > 0:
    st = alph[s%18] + st
    s//=18

for x in '0123456789':
    st = st.replace(x, '*')

for x in 'ABCDEFGH':
    st = st.replace(x, '#')

print(st)