""" p3_18.py """

import numpy as np

datatype = [('name', '=U8'), ('year', int), ('gpa', float)]
students = [('A', 1980, 3.50), ('B', 1970, 2.50), ('C', 2000, 2.00)]
db = np.array(students, dtype=datatype)

db_gpa = np.sort(db, order='gpa')
db_year = np.sort(db, order='year')

print(db)
print(db_gpa)
print(db_year)
