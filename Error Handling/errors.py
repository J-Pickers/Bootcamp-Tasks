# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax Error - fixed by adding partentheses
print ("\n") # Syntax error - fixed by removing indentation. Also missing parentheses again

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Syntax Error - removed indent. Also changed "==" to "="
age = int(age_Str) # Syntax Error - removed indent. Also removed "yeasrs old" from previous line in order to make sense on next line
print(f"I'm {age} years old.") # Syntax Error - removed indent. Also changed format to f-string to resolve concatenation error

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 # Syntax Error - removed indent. Also removed quotes in order for value to be stored as an integer
total_years = age + years_from_now # Syntax Error - removed indent

print (f"The total number of years: {total_years}") # Syntax Error - added parentheses. Corrected answer_years to total_years and used f-string instead of concatenation

# Variable to calculate the total amount of months from the total amount of years and printing the result
extra_months = 6 # This extra variable was needed to account for the extra 6 months in the calculation. Logical error
total_months = total_years*12 + extra_months # Syntax error - corrected vaue name "total" to "total_years"
print (f"In 3 years and 6 months, I'll be {total_months} months old") # Syntax Error - added parentheses. Used f-string instaed of concatenation

#HINT, 330 months is the correct answer

