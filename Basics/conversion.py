'''Pseudocode:
declare num1
declare num2
declare num3
declare string1

convert num1 to integer
convert num2 to float
convert num3 to string
convert string1 to integer

print all 4 on separate lines'''

#Declare variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#Convert variables
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

#Print all on separate lines - I have used triple quotes so as to only need one print statement
print(f'''{num1}
{num2}
{num3}
{string1}''')
