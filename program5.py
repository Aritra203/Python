# program5.py

def is_armstrong_number(number):
    # Convert the number to a string to iterate over digits
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number

# Input from the user
num = int(input("Enter a number: "))

# Check and display result
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")