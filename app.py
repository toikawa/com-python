items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

#x = list(filter(lambda item: item[1] >9, items))
#print(x)
a = [item[1] for item in items if item[1] > 10]
print(a)