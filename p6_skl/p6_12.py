""" p6_12.py """

import pprint
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = load_iris()
df_iris = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
se_target = pd.Series(data=iris['target'], name="target")

df_train, df_test, se_train, se_test = train_test_split(df_iris, se_target)
print(len(df_train))
print(len(df_test))
print(len(se_train))
print(len(se_test))

c_svm = SVC()
c_svm.fit(df_train, se_train)
pred = c_svm.predict(df_test)

pprint.pprint(se_test.to_numpy())
pprint.pprint(pred)

comp = se_test.to_numpy() == pred
pprint.pprint(comp)
acs = accuracy_score(se_test, pred)
print(acs)
