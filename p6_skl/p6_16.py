""" p6_16.py """

from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_true = ["A", "C", "D", "B"]
y_pred = ["B", "C", "B", "A"]

labels = ["A", "C", "D", "B"]

cm = confusion_matrix(y_true, y_pred, labels=labels)
cm_display = ConfusionMatrixDisplay(cm, display_labels=labels)
cm_display.plot()
