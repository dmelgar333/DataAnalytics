# Customer variables

customer_id = 1001
customer_name = 'Demy Melgar'
customer_gender = 'Female'
customer_date_of_birth = '1995-06-15'
drivers_license_number = 'ME123456'
auto_policy_number = 'POL-789012'

# Customer variables using snake_case naming

customer_id = 1001  # stored as a number, could also need to account for letters in some IDs
customer_name = 'Demy Melgar'  # stored as first + last name, could be split into separate variables
customer_gender = 'Female'  # stored as text, may need to account for more options
customer_date_of_birth = '1995-06-15'  # stored as text string, could use a date data type instead
drivers_license_number = 'ME123456'  # stored as text since it contains letters and numbers
auto_policy_number = 'POL-789012'  # stored as text since it contains letters and symbols

my_name = 'Demy Melgar'  # first and last name combined
my_hometown = 'New York, NY'  # city and state combined in one variable

# ============================================================
# LAB 2: Python Reserved Words
# ============================================================

# Full list of Python reserved words that cannot be used as variable names:
# False, None, True, and, as, assert, async, await, break, class,
# continue, def, del, elif, else, except, finally, for, from,
# global, if, import, in, is, lambda, nonlocal, not, or, pass,
# raise, return, try, while, with, yield

# ============================================================
# 5 Reserved Words and their definitions:
# ============================================================

# if -- used to create a conditional statement. It runs a block
# of code only when a certain condition is True.
# Example: if score > 90: print("A grade")

# for -- used to create a loop that repeats a block of code
# for each item in a ^^sequence^^ or ^^iterable^^.
# Example: for name in list_of_names: print(name)

# return -- used inside a ^^function^^ to send a value back
# to wherever the function was called from.
# Example: def add(a, b): return a + b

# True -- a ^^boolean^^ value representing yes or correct.
# Used in conditions and comparisons.
# Example: is_logged_in = True

# import -- used to bring in an external ^^module^^ or library
# so you can use its functions in your code.
# Example: import math