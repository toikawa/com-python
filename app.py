items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

x = list(map(lambda item: item[1] * 1000, items))
print(x)