string = input("Enter a sentence: ")

# Lines 4 - 15 alternate CHARACTERS between upper and lower case
alt_characters = "" # Declares a string to be built upon

# Checks if an index is even, and converts to upper case.
# Converts all odd indexes to lower case
# I have not used enumerate as I am not yet confident in its execution
for index in range(len(string)):
    if index % 2 == 0:
        alt_characters += string[index].upper()
    else:
        alt_characters += string[index].lower() 

print(alt_characters)


# Lines 19 - 30 alternate WORDS between upper and lower case
split = string.split()
alt_words = [] # Declares a list to be built upon

# Again, I have not used enumerate
# .append is needed for a list rather than concatenation
for index in range(len(split)):
    if index % 2 == 0:
        alt_words.append(split[index].lower())
    else:
        alt_words.append(split[index].upper())

print(" ".join(alt_words))
