m=10**9
for x in range(1,2031):
    n=6**100-x; z=0
    for _ in range(100):
        z+=n%6==0
        n//=6
    m=min(m,z)
print(1930+m)