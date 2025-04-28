# Function to reverse a number
def reverse_number(num):
    reversed_num = int(str(num)[::-1]) if num >= 0 else -int(str(-num)[::-1])
    return reversed_num

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to reverse: "))
    print("Reversed Number:", reverse_number(number))