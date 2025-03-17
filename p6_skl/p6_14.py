""" p6_14.py """

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_true = ["cat", "dog", "cat", "cat", "cat", "dog", "dog"]
y_pred = ["dog", "dog", "cat", "cat", "cat", "dog", "cat"]
labels = ["cat", "dog"]

cm = confusion_matrix(y_true, y_pred, labels=labels)
cm_display = ConfusionMatrixDisplay(cm, display_labels=labels)
cm_display.plot()
plt.grid(False)

tp, fn, fp, tn = cm.flatten()
print(cm)
print(f"TP:{tp}, FN:{fn}, FP:{fp}, TN:{tn}")
