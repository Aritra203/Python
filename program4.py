def sum_from_m_to_n(m, n):
    """
    Calculate the sum of integers from m to n (inclusive).
    """
    if m > n:
        return 0
    return sum(range(m, n + 1))

# Example usage
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))
result = sum_from_m_to_n(m, n)
print(f"The sum from {m} to {n} is: {result}")