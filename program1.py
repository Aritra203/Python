# Program to find the larger number between two numbers

# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and find the larger one
if num1 > num2:
    print(f"The larger number is: {num1}")
elif num2 > num1:
    print(f"The larger number is: {num2}")
else:
    print("Both numbers are equal.")