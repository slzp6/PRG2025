""" p6_3.py """

from sklearn.datasets import load_iris

iris = load_iris()

print(iris.keys())
print(iris['data'].shape)
print(iris['target'].shape)
