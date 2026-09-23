f = open('3.txt')
clients = {}
for l in f:
    client = l.strip().split()
    if client[0] in clients:
        clients[client[0]]+=int(client[1])
    else:
        clients[client[0]] = int(client[1])
cnt = 0
for c in clients:
    if clients[c] % 21 and clients[c] < 0:
        cnt+=clients[c]

print(cnt)
