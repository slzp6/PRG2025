""" p1_12.py """

X = 50
print(20 < X < 90)
# print(X > 20 and X < 90)　と同じ
# R1716: Simplify chained comparison between the operands

print(X > 30 or X < 40)

print(X <= 30)
# (not X > 30) と同じ
