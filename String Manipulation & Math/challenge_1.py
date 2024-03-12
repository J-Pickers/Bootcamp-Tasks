# Import the math module, for use of the .sqrt function
import math

# Receive side lengths from user, stored as integers
side1 = int(input("Please enter the length of one side : "))
side2 = int(input("Please enter the length of another side : "))
side3 = int(input("Please enter the length of the last side : "))

# Calculate the area of the triangle
s = (side1 + side2 + side3)/2
area = math.sqrt(s * (s - side1)*(s - side2)*(s - side3))

# Print the result (\n for readability)
print(f"\nThe area of a triangle of side lengths {side1}, {side2}, and {side3} will have an area of {area}!\n")
