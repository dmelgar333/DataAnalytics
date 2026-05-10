# Movie List
# Author: Demy Melgar

# Create a list of favorite movies
movie_list = [
    'The Dark Knight',
    'Interstellar',
    'Get Out',
    'Coco',
    'The Pursuit of Happyness',
    'Black Panther'
]

# Print descriptive statement using len()
print(f"The list movie_list includes my top {len(movie_list)} favorite movies")

# Print the complete list
print(movie_list)

# ============================================================
# Print sorted list two ways
# ============================================================

# Using sorted() function
print(sorted(movie_list))
print(movie_list)
# OBSERVATION: sorted() prints a sorted version but does NOT
# change the original list -- movie_list stays in original order

# Using .sort() method
movie_list.sort()
print(movie_list)
# OBSERVATION: .sort() permanently changes the original list
# so movie_list is now sorted for good

# ============================================================
# Add a new movie using .append()
# ============================================================
movie_list.append('Parasite')
print(f"The list movie_list includes my top {len(movie_list)} favorite movies")
print(movie_list)