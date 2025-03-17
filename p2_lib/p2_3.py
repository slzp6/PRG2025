""" p2_3.py """


def my_func(valx, valy):
    """Takes two numbers and exchange them."""
    return valy, valx


A = 10
B = 20
print(A, B)
A, B = my_func(A, B)
print(A, B)
