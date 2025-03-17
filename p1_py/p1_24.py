""" p1_24.py """

fruits = ["apple", "banana", "cranberry"]
weights = [10, 20, 30]

# d_fruits = {key: value for (key, value) in zip(fruits, weights)}
d_fruits = dict(zip(fruits, weights))
print(d_fruits)
