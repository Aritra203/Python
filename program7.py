# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        return "Invalid binary number"

# Input from the user
binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)

print(f"The decimal equivalent of binary {binary_input} is: {decimal_output}")