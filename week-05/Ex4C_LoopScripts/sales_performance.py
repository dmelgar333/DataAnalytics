# Sales Performance
# Author: Demy Melgar

# Sales data list of tuples
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

# BONUS - track total sales
total_sales = 0

# ============================================================
# Loop through sales data
# ============================================================
for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")

    if sales > 5000:
        print(" ^ Top performer!")

    # Add to total
    total_sales += sales

# Print total after loop
print(f"\nTotal sales across all employees: ${total_sales:,.2f}")