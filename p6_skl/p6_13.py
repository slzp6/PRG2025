""" p6_13.py """

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x = [3.01, 3.25, 3.30, 3.55, 3.78, 3.90, 4.10]
y = [1.51, 1.73, 1.93, 2.15, 2.30, 2.50, 2.70]
df = pd.DataFrame({"x": x, "y": y})
print(df)

x_train, x_test, y_train, y_test = \
train_test_split(df[["x"]],df[["y"]], random_state=2)

print("--- train")
print(x_train)
print(y_train)

print("--- test")
print(x_test)
print(y_test)

lr = LinearRegression()
lr.fit(x_train, y_train)

print("coeff:", lr.coef_)
print("intercept:", lr.intercept_)
print("train:", lr.score(x_train, y_train))
print("test:", lr.score(x_test, y_test))

fig1, ax1 = plt.subplots()
ax1.scatter(x_train, y_train, s=300, marker='o')
ax1.scatter(x_test, y_test, s=300, marker='s')
plt.savefig("p6_13a.png")

fig2, ax2 = plt.subplots()
ax2.scatter(x_train, y_train, s=300, marker='o')
ax2.scatter(x_test, y_test, s=300, marker='s')
ax2.plot(x_train, lr.predict(x_train), linestyle='--')
# ax2.plot(x_test, lr.predict(x_test))
plt.savefig("p6_13b.png")
