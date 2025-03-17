""" p6_11.py """

from sklearn.metrics import accuracy_score

y_pred = [0, 1, 2, 3, 2, 2]
y_true = [0, 1, 2, 2, 1, 2]
acs = accuracy_score(y_true, y_pred)
acs_nf = accuracy_score(y_true, y_pred, normalize=False)

print(acs)
print(acs_nf)
