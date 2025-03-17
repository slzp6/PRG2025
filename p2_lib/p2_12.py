""" p2_12.py """
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)
