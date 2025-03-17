""" p4_21.py """

import seaborn as sns

anscombe = sns.load_dataset('anscombe')
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", \
           data=anscombe, col_wrap=2, ci=95, palette="pastel", height=2.5)
