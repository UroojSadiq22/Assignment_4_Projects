# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def double_numbers(numbers: list) -> list:
    """Returns a list with each number doubled."""
    for i in range(len(numbers)):
        numbers[i] *=2
    return numbers

def main():
    """Main function to demonstrate the double_numbers function."""
    print("This tool doubles each number in a list.")
    print("\t")
    
    numbers: list = [1, 2, 3, 4]
    print("\t")
    print(f"The actual numbers are {numbers}")
    
    doubled_numbers: list = double_numbers(numbers)
    
    print("\t")
    print(f"The doubled numbers are {doubled_numbers}")

if __name__ == '__main__':
    main()
