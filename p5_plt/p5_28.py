""" p5_28.py """

import seaborn as sns

sns.set_theme()
anscombe = sns.load_dataset('anscombe')
sns.lmplot(x="x",
           y="y",
           col="dataset",
           hue="dataset",
           data=anscombe,
           col_wrap=2,
           ci=95,
           palette="Dark2",
           height=3.0)
