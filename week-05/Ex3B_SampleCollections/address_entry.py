# Address Entry
# Author: Demy Melgar

# Define contact_info dictionary
contact_info = {
    'name': 'Demy Melgar',
    'address': '123 Main Street',
    'city': 'New York',
    'state': 'NY',
    'zip': '10001'
}

# Print formatted mailing address
print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

# ============================================================
# Remove the name key
# ============================================================
del contact_info['name']
print(contact_info)

# ============================================================
# Add full_name as a nested dictionary
# ============================================================
full_name = {
    'first name': 'Demy',
    'last name': 'Melgar'
}

# Use .update() to add honorific
full_name.update({'honorific': 'Ms.'})
print(full_name)

# Use .update() to add full_name to contact_info
contact_info.update({'full_name': full_name})
print(contact_info)

# Print updated formatted address
print(f"{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")