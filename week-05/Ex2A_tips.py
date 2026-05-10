# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate the unknown
total_due = food_cost + tax + tip
# Display the results
print("The total due is " + str(total_due))
#python cannot mix text and numbers without str

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print("The total due is " + str(total_due))
# str() converts the number to text so it can be joined with a string using +

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("Tip is " + str(tip))
print("Total due is " + str(total_due))

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print("The total due is " + str(total_due))
# str() converts the number to text so it can be joined with a string using +

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))