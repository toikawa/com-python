from timeit import timeit

code1 = '''
def calcurate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age

try:
    calcurate_xfactor(0)
except ValueError as error:
    pass
'''
code2 = '''
def calcurate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calcurate_xfactor(-1)
if xfactor == None:
    pass

'''


duration1 = timeit(code1, number=10000)
duration2 = timeit(code2, number=10000)

print("code1 runtime duration=", duration1)
print("code2 runtime duration=", duration2)







