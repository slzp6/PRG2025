""" p2_17.py """
import pprint

N = [80, 40, 30, 20, 10]
print(type(N))
pprint.pprint(dir(N), width=80, compact=True)
print(N)
print(N.pop())
print(N)
