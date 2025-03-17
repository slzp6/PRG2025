""" p6_20.py """

import random
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

random.seed(42)

y_true = []
for i in range(1000):
    y_true.append(random.randint(1, 10))

y_pred = y_true
y_pred2 = random.sample(y_true, len(y_true))

labels = []
for i in range(1, 11):
    labels.append(i)

cm = confusion_matrix(y_true, y_pred, labels=labels)
cm_display = ConfusionMatrixDisplay(cm, display_labels=labels)
cm_display.plot()

cm2 = confusion_matrix(y_true, y_pred2, labels=labels)
cm2_display = ConfusionMatrixDisplay(cm2, display_labels=labels)
cm2_display.plot()

print("true: ", y_true[:10])
print("pred: ", y_pred[:10])
print("pred2:", y_pred2[:10])
