""" p1_13.py """

a = [10, 3.14, "ouj"]
b = [10, 3.14, "ouj"]
c = a

print(a is c)
print(a is b)
print(a == b)

print(id(a))
print(id(b))
print(id(c))
