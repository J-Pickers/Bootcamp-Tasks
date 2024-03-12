# Ask user for 3 numbers, ensuring they are stored as integers
user_num1 = int(input("Please enter your first number : "))
user_num2 = int(input("Please enter your second number : "))
user_num3 = int(input("Please enter your third number : "))

# Store the sum of all three
sum = user_num1 + user_num2 + user_num3

# Store the value of the first number minus the second 
first_minus_second = user_num1 - user_num2

# Store the value of the third number multiplied by the first
third_times_first = user_num3 * user_num1

# Store the value of the sum, divided by the third number
sum_divided = sum / user_num3

# Print out the answers - I am using a triple-quoted f-string for readability
print(f"""
      
The sum of all your numbers is {sum}!
      
{user_num1} minus {user_num2} is {first_minus_second}!

{user_num3} times {user_num1} is {third_times_first}!

{sum} divided by {user_num3} is {sum_divided}!

""")
