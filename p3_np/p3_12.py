""" p3_12.py """

import numpy as np

a = np.array([80, 40, 30, 20, 20])
b = np.sort(a)
print(a)
print(b)

sort_q = np.sort(a, kind="quicksort")
sort_m = np.sort(a, kind="mergesort")
sort_h = np.sort(a, kind="heapsort")
sort_s = np.sort(a, kind="stable")

print(sort_q)
print(sort_m)
print(sort_h)
print(sort_s)
