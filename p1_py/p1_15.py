""" p1_15.py """

X, Y = 50, 30

MIN = X if X < Y else Y
print(MIN)

MIN = (Y, X)[X < Y]
print(MIN)
