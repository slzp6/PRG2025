""" p2_10.py """


def my_func(**kwargs):
    """Collects all the keyword arguments in a dictionary."""
    print(kwargs)
    print(type(kwargs))


dc = {'ka': 40, 'kb': 50, 'kc': 60}

# '**' unpacks a dictionary into keyword arguments.
my_func(**dc)
