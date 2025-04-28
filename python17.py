# Get user input as a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Find numbers divisible by 10
divisible_by_10 = [num for num in numbers if num % 10 == 0]

# Display the result
print("Numbers divisible by 10:", divisible_by_10)