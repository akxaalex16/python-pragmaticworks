import pandas as pd

# # we are trying to reference a file that is currently not in the file that we are using
# # reference to a file containing python functions, classes, and variables

# # function in calculator.py


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

# # current file
# import calculator

# calculator.add(10, 2)


# # you can rename modules used in your code
# import calculator as calc

# calc.add(10, 2)
# calc.subtract(10, 2)


# # the from statement allows you to narrow down the
# #     scope of what you need to pull in as the files get bigger and bigger
# # from allows you to import specific attributes without needed to specify the module first

# from calculator import add

# add(10, 2)


# # all attributes can be imported with *
# from calculator import *

# add(10, 2)
# subtract(10, 2)


# import third party packages below by searching for them in the packages tab
# imported pandas at the top of current file to be used

a = [2, 3, 6, 9, 16]

output = pd.Series(a)

print(a)

