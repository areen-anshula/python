
from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    item_name, price = input().rsplit(' ', 1)
    price = int(price)

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item_name, net_price in items.items():
    print(item_name, net_price)
