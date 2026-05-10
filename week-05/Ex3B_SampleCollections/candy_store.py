# Candy Store
# Author: Demy Melgar

# Create two tuples
candy_types = ('Skittles', 'Starburst', 'Jolly Ranchers')
fruity_flavors = ('Strawberry', 'Watermelon', 'Mango')

# Create a set of candy combinations
candy_combos = set()
candy_combos.add(candy_types[0] + ' ' + fruity_flavors[0])
candy_combos.add(candy_types[0] + ' ' + fruity_flavors[1])
candy_combos.add(candy_types[1] + ' ' + fruity_flavors[2])
candy_combos.add(candy_types[2] + ' ' + fruity_flavors[0])
candy_combos.add(candy_types[2] + ' ' + fruity_flavors[1])

# Print candy options
print("Today's candy options include:")
print(candy_combos)

# Print multiple times
print("Today's candy options include:")
print(candy_combos)

print("Today's candy options include:")
print(candy_combos)

# OBSERVATION: The order of items changes every time you print
# because sets are unordered -- they do not keep a fixed order