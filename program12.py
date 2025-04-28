# Program to convert Fahrenheit to Celsius

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Input from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)

# Display the result
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")