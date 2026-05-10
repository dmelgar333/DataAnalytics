# Min Max - Find smallest and largest of three numbers
# Author: Demy Melgar

a = 45
b = 12
c = 78

# ============================================================
# Find the smallest number
# ============================================================
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# ============================================================
# Find the largest number
# ============================================================
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# ============================================================
# Display results
# ============================================================
print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")