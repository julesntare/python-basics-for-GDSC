""" Errors handling in python 

    we have 2 kinds of errors in python:
        1. Syntax error
        2. Exceptions

"""

# syntax errors examples

# indentation error
amount = 18

# if amount < 16:
# print("You're not eligible to attend this event")
# else:
#     print("You can lead the event")


# other syntax error
# ages = {
#     'pam': 24,
#     'jim': 24
#     'michael': 43
# }
# print(f'Michael is {ages["michael"]} years old.')

# other syntax errors
# message = 'don't'
# message = "This is an unclosed string


# Exceptions

# Division By Zero Error (ZeroDivisionError)
amount = 10000
# print(amount / 0)

# file not found
# file = open("gdsc_python_session.ppt", "r")

# raising exceptions

# value error
number = 34
# if number > 13:
#     raise ValueError('Chill Bro, we need teenagers. You\'re in retirement ages')

# type error
isValid = "True"
# if not type(isValid) is bool:
#   raise TypeError("Only Boolean is allowed")

# key error (from dictionaries)
Rate = {'bottle': 5, 'chair': 1200, 'pen':50}
item = input("Enter the item: ")
print(Rate[item])
if Rate[item]:
    print(f"The rate of {item} is {Rate[item]}")
else:
    raise KeyError("The price of is not found ")