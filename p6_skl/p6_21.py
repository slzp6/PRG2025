""" p6_21.py """
#
# Make sure to install pycaret
# https://pycaret.org/
#

# pylint: disable=pointless-string-statement
'''
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve

X, y = make_classification(n_samples=1000,
                           n_classes=2,
                           n_features=10,
                           n_informative=2,
                           n_redundant=4,
                           random_state=42)
trainX, testX, trainy, testy = train_test_split(X,
                                                y,
                                                test_size=0.5,
                                                random_state=42)

print(trainX.shape, trainy.shape)
print(testX.shape, testy.shape)

# model = LogisticRegression(solver='lbfgs')
# model = LogisticRegression(solver='newton-cg')
# model = LogisticRegression(solver='sag')
model = LogisticRegression()

model.fit(trainX, trainy)
lr_probs = model.predict_proba(testX)
lr_probs = lr_probs[:, 1]

yhat = model.predict(testX)
lr_precision, lr_recall, thresholds = precision_recall_curve(testy, lr_probs)

fig, ax = plt.subplots()
ax.plot(lr_recall, lr_precision, label='Logistic')
ax.set_title('precision-recall curve')
ax.set_xlabel('recall')
ax.set_ylabel('precision')
# plt.show()
plt.savefig("p6_21.png")

'''
