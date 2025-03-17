""" p2_8.py """


def my_func(*args):
    """Collects all the positional arguments in a tuple."""
    print(args)


tpl = (400, 500, 600)

# '*' unpacks a tuple into positional arguments
my_func(*tpl)
