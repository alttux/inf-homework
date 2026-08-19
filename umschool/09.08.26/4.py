import math

f = open('4.txt')
items = {}
for line in f:
    line = line.strip()
    if not line:
        continue
    item_id, rest = line.split(':')
    quantity, price = rest.split(',')
    quantity = int(quantity)
    price = int(price)
    revenue = quantity * price
    if item_id in items:
        items[item_id][0] += quantity
        items[item_id][1] += revenue
    else:
        items[item_id] = [quantity, revenue]

items = {k: v for k, v in items.items() if v[0] >= 1000}

for item_id in items:
    quantity, revenue = items[item_id]
    if quantity > 1250:
        items[item_id] = [quantity * 0.85, revenue * 0.85]

revenues = [v[1] for v in items.values()]
diff = max(revenues) - min(revenues)

if diff == int(diff):
    print(int(diff))
else:
    print(math.floor(diff + 0.5))
