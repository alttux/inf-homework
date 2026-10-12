def R(n):
    b=bin(n)[2:]
    b+=b[-3:] if n%3==0 else bin(n%3*3)[2:]
    return int(b,2)
r=min(abs(R(n)-130) for n in range(1,2000))
print(max(n for n in range(1,2000) if abs(R(n)-130)==r))