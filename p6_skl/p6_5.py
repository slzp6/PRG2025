""" p6_5.py """

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df_iris = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
se_target = pd.Series(data=iris['target'], name="target")

fig, ax = plt.subplots()
scatter = ax.scatter(df_iris.iloc[:, 0], df_iris.iloc[:, 1], c=se_target)
ax.set(xlabel=iris['feature_names'][0], ylabel=iris['feature_names'][1])
fig = ax.legend(scatter.legend_elements()[0], iris['target_names'])
plt.savefig("p6_5.png")
# ax.plot()
