""" p6_8.py """

import seaborn as sns

df = sns.load_dataset("iris")
pp = sns.pairplot(df, hue='species', markers=["o", "*", "v"])
pp.savefig("p6_8.png")
#
