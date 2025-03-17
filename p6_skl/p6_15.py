""" p6_15.py """

from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_true = ["A", "C", "D", "B"]
y_pred = ["B", "C", "B", "A"]

cm = confusion_matrix(y_true, y_pred)
print(cm)
cm_display = ConfusionMatrixDisplay(cm)
cm_display.plot()
