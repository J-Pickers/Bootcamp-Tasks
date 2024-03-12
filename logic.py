# This program is intended to calculate how many days old the user is.
# However, it fails to take into account leap years and the variety
# of lengths a month can be.

print("This program can caluclate how many days old you are!")
years = int(input("Enter your age in years: "))
months = int(input("Enter how many months since your birthday: "))
days = int(input("Enter how many days extra on top of the months: "))

total = years * (365 + months) * 30 + days
# This calculation is also incorrect, as the parentheses are in the wrong place.
# The following would be correct:
# total = (years * 365)+(months * 30)+days

print(f"You are {total} days old!")
