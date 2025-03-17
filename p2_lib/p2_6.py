""" p2_6.py """


def my_func(i, j, /, *, x, y, z):
    """Takes five numbers and returns their sum."""
    print(i + j + x + y - z)


my_func(10, 20, x=30, y=40, z=50)
my_func(10, 20, z=50, x=30, y=40)
