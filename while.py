'''This file takes numbers as user input, and returns the average.
   -1 is to be used to execute the calculation.'''

# Declare variables ready to store user input
number, total, count = 0, 0, 0

# For loop calculates total of user inputs
while True:
    number = float(input("Please enter a number: "))

    # Break loop if number is -1
    if number == -1:
        break

    total += number
    count += 1

# Calculate and print average
average = total / count

print(f"The average of your numbers is {average}")
