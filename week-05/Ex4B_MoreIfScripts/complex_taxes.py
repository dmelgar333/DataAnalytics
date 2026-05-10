# Complex Taxes Calculator
# Author: Demy Melgar

# ============================================================
# Calculate gross pay (from pay_rules.py)
# ============================================================
pay_rate = 17.30
hours_worked = 45
filing_status = 'single'

if hours_worked > 40:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_weekly_pay = regular_pay + overtime_pay
else:
    gross_weekly_pay = pay_rate * hours_worked

# Calculate annual gross pay (52 weeks in a year)
annual_gross = gross_weekly_pay * 52

# ============================================================
# Determine tax rate based on filing status and income
# ============================================================
if filing_status == 'single':
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == 'joint':
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Calculate weekly tax and net pay
weekly_tax = gross_weekly_pay * tax_rate
net_pay = gross_weekly_pay - weekly_tax

# ============================================================
# Display results
# ============================================================
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is ${format(gross_weekly_pay, '.2f')}")
print(f"Your filing status is {filing_status}")
print(f"Your estimated annual gross pay is ${format(annual_gross, '.2f')}")
print(f"Your tax rate is {format(tax_rate, '.0%')}")
print(f"Your tax withholding for the week is ${format(weekly_tax, '.2f')}")
print(f"Your net pay is ${format(net_pay, '.2f')}")