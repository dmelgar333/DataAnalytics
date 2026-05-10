# Greeting based on time of day
# Author: Demy Melgar

# Define current hour (0-23)
current_hour = 14

# ============================================================
# Greeting based on hour including late night condition
# ============================================================
if current_hour >= 23 or current_hour < 4:
    print("What are you doing up so late??")
elif current_hour < 10:
    print("Good morning!")
elif current_hour < 17:
    print("Good day!")
else:
    print("Good evening!")