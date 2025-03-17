""" p6_17.py """

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris['data']
y = iris['target']

X_train, X_test, y_train, y_test = \
train_test_split(X, y, test_size=0.50, random_state=100)

clf = DecisionTreeClassifier(random_state=100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

lclass = [0, 1, 2]
labels = iris['target_names']

cm = confusion_matrix(y_test, y_pred, labels=lclass)
cm_display = ConfusionMatrixDisplay(cm, display_labels=labels)
cm_display.plot()
