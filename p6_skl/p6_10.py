""" p6_10.py """

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

df_iris = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
se_target = pd.Series(data=iris['target'], name="target")

df_train, df_test, se_train, se_test = train_test_split(df_iris, se_target)

print(len(df_train))
print(len(df_test))
print(len(se_train))
print(len(se_test))
