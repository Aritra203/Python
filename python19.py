# Program to print the special pattern

n = int(input("Enter the number of rows: "))  # Number of rows
for i in range(1, n + 1):
    print((str(i) + ' ') * i)