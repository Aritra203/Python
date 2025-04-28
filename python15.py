# Program to print even numbers from 2 to n

def print_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i, end=" ")

# Input from the user
n = int(input("Enter the value of n: "))
print("Even numbers from 2 to", n, "are:")
print_even_numbers(n)