# Ranked List
# Author: Demy Melgar

# Create a list of at least 5 items
favorite_foods = ['tacos', 'ramen', 'jerk chicken', 
                  'sushi', 'pizza', 'empanadas']

# Use enumerate() with for loop starting at 1
for index, food in enumerate(favorite_foods, 1):
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")

# ============================================================
# BONUS - Print list in reverse order still numbered 1 through 6
# ============================================================
print("\nReverse order:")
for index, food in enumerate(reversed(favorite_foods), 1):
    print(f"{index}. {food}")