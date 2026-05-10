# Savings Goal
# Author: Demy Melgar

# Define variables
bank_balance = 500.00
savings_goal = 2000.00
weekly_savings = 150.00

# ============================================================
# While loop to reach savings goal
# ============================================================
while bank_balance < savings_goal:
    bank_balance += weekly_savings

    if bank_balance >= savings_goal * 0.75:
        treat = weekly_savings * 0.05
        bank_balance -= treat
        print(f"So close! After treating myself, my balance is up to ${format(bank_balance, '.2f')}")
    elif bank_balance >= savings_goal * 0.50:
        print(f"Almost there! This week my balance is up to ${format(bank_balance, '.2f')}")
    else:
        print(f"This week my balance increased to ${format(bank_balance, '.2f')}")

print(f"Goal met! My current balance is ${format(bank_balance, '.2f')}")