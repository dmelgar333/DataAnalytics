# Pay Rules - Gross Pay Calculator
# Author: Demy Melgar
# Formula: regular pay + overtime pay if hours > 40
# Overtime rate is 1.5 times regular rate

# Define variables
pay_rate = 17.30
hours_worked = 45

# ============================================================
# Calculate gross pay
# ============================================================
if hours_worked > 40:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
    print(f"You worked {hours_worked} hours this period")
    print(f"Regular pay: ${format(regular_pay, '.2f')}")
    print(f"Overtime hours: {overtime_hours} at ${format(pay_rate * 1.5, '.2f')}/hr")
    print(f"Gross pay: ${format(gross_pay, '.2f')}")
else:
    gross_pay = pay_rate * hours_worked
    print(f"You worked {hours_worked} hours this period")
    print(f"Gross pay: ${format(gross_pay, '.2f')}")