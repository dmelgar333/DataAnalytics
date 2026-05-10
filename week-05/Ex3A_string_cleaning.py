# Description: String cleaning exercises
# Author: Demy Melgar

# Starting messy data
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# ============================================================
# Convert names to lowercase using .lower()
# ============================================================
print(name_1.lower())   # priya sharma
print(name_2.lower())   # bob nguyen
print(name_3.lower())   # latonya williams

# ============================================================
# Convert names to title case using .title()
# ============================================================
print(name_1.title())   # Priya Sharma
print(name_2.title())   # Bob Nguyen
print(name_3.title())   # Latonya Williams

# ============================================================
# Remove $ from salary strings using .replace()
# ============================================================
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")
print(salary_1_clean)           # 82,500
print(salary_2_clean)           # 74,000
print(type(salary_1_clean))     # still a string!
# To do math we would also need to remove the comma
# and convert to int or float

# ============================================================
# Chain .replace() and int() to get a usable integer
# ============================================================
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int)             # 82500
print(type(salary_1_int))       # now it is an integer!