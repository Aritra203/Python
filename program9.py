import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Input the sides of the triangle
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

# Check if the sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    area = calculate_area(a, b, c)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The entered sides do not form a valid triangle.")