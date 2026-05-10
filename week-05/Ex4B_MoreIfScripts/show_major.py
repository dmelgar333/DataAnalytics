# Show Major - Display major name and office location
# Author: Demy Melgar

student_name = 'Demy Melgar'
student_major = 'CSCI'

# ============================================================
# Lookup major name and office location
# ============================================================
if student_major == 'BIOL':
    major_name = 'Biology'
    office = 'Science Bldg, Room 310'
elif student_major == 'CSCI':
    major_name = 'Computer Science'
    office = 'Sheppard Hall, Room 314'
elif student_major == 'ENG':
    major_name = 'English'
    office = 'Kerr Hall, Room 201'
elif student_major == 'HIST':
    major_name = 'History'
    office = 'Kerr Hall, Room 114'
elif student_major == 'MKT':
    major_name = 'Marketing'
    office = 'Westly Hall, Room 310'
else:
    major_name = '<unknown>'
    office = ''

# ============================================================
# Display results
# ============================================================
if office:
    print(f"{student_name} is majoring in {major_name}")
    print(f"Department office: {office}")
else:
    print(f"{student_name} is majoring in {major_name}")
    print("No office location available")