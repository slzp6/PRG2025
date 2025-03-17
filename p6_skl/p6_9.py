""" p6_9.py """

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df_iris = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
se_target = pd.Series(data=iris['target'], name="target")

print(df_iris.head(3))
print(se_target.head(3))

print(df_iris.describe())
