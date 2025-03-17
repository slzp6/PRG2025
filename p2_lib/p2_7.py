""" p2_7.py """


def my_func(*args):
    """Collects all the positional arguments in a tuple."""
    print(args)
    print(type(args))


my_func(100, 200, 300)
