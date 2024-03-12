'''Pseudocode:
receive name input
receive age input
receive house number input
receive street name input

print text using f-string to format the sentence'''

#Receive name input
name = input("Enter your name : ")

#Receive age input
age = input("Enter your age : ")

#Receive house number input
house_number = input("Enter your house number : ")

#Receive street name input
street_name = input("Enter your street name : ")

#Print text using f-string to format, and \n for presentation
print(f"\nThis is {name}. They are {age} years old and live at house number {house_number} on {street_name}.")