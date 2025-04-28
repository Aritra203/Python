# Function to check if the first and last elements of a list are the same
def is_first_and_last_same(lst):
    if not lst:
        return False  # Return False for an empty list
    return lst[0] == lst[-1]

# Example usage
sample_list = [10, 20, 30, 10]
result = is_first_and_last_same(sample_list)
print(f"Is the first and last element the same? {result}")