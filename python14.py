# Program to calculate addition and subtraction of complex numbers

# Function to add two complex numbers
def add_complex(c1, c2):
    return c1 + c2

# Function to subtract two complex numbers
def subtract_complex(c1, c2):
    return c1 - c2

# Input complex numbers
complex1 = complex(input("Enter the first complex number (e.g., 3+4j): "))
complex2 = complex(input("Enter the second complex number (e.g., 1+2j): "))

# Perform addition and subtraction
addition_result = add_complex(complex1, complex2)
subtraction_result = subtract_complex(complex1, complex2)

# Display results
print(f"Addition of {complex1} and {complex2} is: {addition_result}")
print(f"Subtraction of {complex1} and {complex2} is: {subtraction_result}")