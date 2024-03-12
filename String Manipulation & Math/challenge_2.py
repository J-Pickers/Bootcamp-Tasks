# Receive favourite restaurant
string_fav = input("Please enter your favourite restaurant : ")

# Receive favourite number, stored as integer
int_fav = int(input("Please enter your favourite number : "))

# Print both out
print(f"\nYour favourite restaurant is {string_fav}!")
print(f"\nYour favourite number is {int_fav}!\n")

# Attempting to cast would look like this:

# cast = int(string_fav)

# If python tries to execute this, a ValueError will occur as strings containing non-numerical characters cannot be cast as an integer.
