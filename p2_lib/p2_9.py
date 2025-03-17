""" p2_9.py """


def my_func(**kwargs):
    """Collects all the keyword arguments in a dictionary."""
    print(kwargs)
    print(type(kwargs))


my_func(ka=10, kb=20, kc=30)
