import math

a = float(input())

print(math.ceil(a))
a = int(input())
b = int(input())
if a < b:
    print(a)
elif a == b:
    print('Chisla ravny')
else:
    print(b)
