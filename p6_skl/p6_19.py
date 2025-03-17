""" p6_19.py """

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC

iris = load_iris()
X = iris['data']
y = iris['target']

X_train, X_test, y_train, y_test = \
train_test_split(X, y, test_size=0.50, random_state=100)

clf = SVC(random_state=100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

cr = classification_report(y_test, y_pred, target_names=iris['target_names'])
print(cr)
