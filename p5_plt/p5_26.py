""" p5_26.py """

import seaborn as sns

sns.set_theme()

df = sns.load_dataset("iris")

print(type(df))
print(df.head())

iris = sns.relplot(data=df, x="sepal_length", y="sepal_width", \
            hue="species", style="species")
iris.figure.savefig("test_sns.png")
