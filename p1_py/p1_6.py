""" p1_6.py """

f = {"apple", "banana", "coconut"}
f.add("dekopon")
print(f)
print(type(f))

ff = frozenset({"apple", "banana", "coconut"})
#  ff.add("dekopon")  'frozenset' object has no attribute 'add'
print(ff)
print(type(ff))
