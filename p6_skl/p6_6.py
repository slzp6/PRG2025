""" p6_6.py """

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df_iris = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
se_target = pd.Series(data=iris['target'], name="target")

fig, ax = plt.subplots()
scatter = ax.scatter(df_iris.iloc[:, 2], df_iris.iloc[:, 3], c=se_target)
ax.set(xlabel=iris['feature_names'][2], ylabel=iris['feature_names'][3])
fig = ax.legend(scatter.legend_elements()[0], iris['target_names'])
# ax.plot()
plt.savefig("p6_6.png")
