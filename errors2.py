# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Syntax error - added quotes to correctly store word as a string
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth") # Syntax error - added parentheses as well as "f" to denote f-string.
# Also swapped last two variables to make sense - logical error

print(full_spec) # Syntax error - added missing parentheses
