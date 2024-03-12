# I like to use "\n" at the end of my print statements to make them more readable

# Receive user sentence
str_manip = input("Please enter a sentence : ")

# Calculate string length
str_length = len(str_manip)

# Print string length
print(f"\nYour sentence is {str_length} characters long!\n")

# Find the last letter of the string
last_letter = str_manip[-1:-2:-1]

# Replace all instances of the last letter
print(str_manip.replace(last_letter, "@") + "\n")

# Print last 3 charatcers backwards
print(str_manip[-1:-4:-1] + "\n")

# Slice last 2 characters
last_two = str_manip[-1:-3:-1]

# Print a 5-letter word consisting of first 3 and last 2 characters
print(str_manip[:3] + last_two[::-1] + "\n")

