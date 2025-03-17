""" p1_21.py """

fruits = ["apple", "banana", "coconut", "dekopon"]

long_names = []
for i in fruits:
    if len(i) > 6:
        long_names.append(i)
print(long_names)

long_names_lc = [j for j in fruits if len(j) > 6]
print(long_names_lc)
