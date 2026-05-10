# Description: This script tests various numeric conversion techniques
# Author: Demy Melgar

# Define starting variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# ============================================================
# Print each variable and its type
# ============================================================
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# ============================================================
# Variable A transformations
# ============================================================
# Cast as integer - ERROR because it has a decimal point and spaces
# int(a)  # ValueError: invalid literal for int() with base 10

# Cast as float - works after stripping spaces
a_float = float(a)
print(a_float, type(a_float))

# Cast float then integer - works!
a_int = int(float(a))
print(a_int, type(a_int))

# Strip leading/trailing spaces
print(a.strip())

# ============================================================
# Variable B transformations
# ============================================================
# Cast as integer - works!
b_int = int(b)
print(b_int, type(b_int))

# Cast as float - works!
b_float = float(b)
print(b_float, type(b_float))

# ============================================================
# Variable C transformations
# ============================================================
# Cast as integer - ERROR because it contains letters
# int(c)  # ValueError: invalid literal for int() with base 10

# Cast as float - ERROR because it contains letters
# float(c)  # ValueError: could not convert string to float

# Use slicing to get just the numeric portion "402"
c_num = int(c[0:3])
print(c_num, type(c_num))
# indexing starts at 0 so c[0:3] gives us characters 0,1,2 = "402"

# ============================================================
# Variable D transformations
# ============================================================
# Cast as integer - ERROR because it contains letters
# int(d)  # ValueError: invalid literal for int() with base 10

# Cast as float - ERROR because it contains letters
# float(d)  # ValueError: could not convert string to float

# Use slicing to get just the numeric portion "5"
d_num = int(d[7])
print(d_num, type(d_num))
# d[7] gives us the character at index 7 which is "5"

# Strip leading/trailing spaces
print(d.strip())