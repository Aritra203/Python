def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Input from user
try:
    n_terms = int(input("Enter the number of terms: "))
    if n_terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        fibonacci_series(n_terms)
except ValueError:
    print("Invalid input! Please enter an integer.")