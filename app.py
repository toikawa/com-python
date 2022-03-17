items = [
    "Product1": 10,
    "Product2": 9,
    "Product3":12
]

items.sort(key=lambda items:items[1])
print(items)