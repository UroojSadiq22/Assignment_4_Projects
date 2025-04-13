# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n:int, lower:int, upper:int) -> bool:
    """Check if a number is within a specified range."""
    if n>= lower and n <= upper:
        return True

    return False

def main():
    """Main function to get user input and check if it's in range."""
    print("This tool checks if the number you enter is in the specified range.")
    print("\t")

    user_input = int(input("Enter a number to check: "))
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    print(in_range(user_input, lower_bound, upper_bound))

if __name__ == '__main__':
    main()
    