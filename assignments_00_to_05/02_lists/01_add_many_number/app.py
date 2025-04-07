# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers(numbers: list) -> int:
    """Returns the sum of a list of numbers."""
    total: int = 0
    for number in numbers:
        total += number
    return total

def main():
    """Main function to demonstrate the add_many_numbers function."""
    print("This tool adds a list of numbers.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    # Example list of numbers to add
    numbers: list = [1, 2, 3, 4, 5]
    
    total: int = add_many_numbers(numbers)
    
    print("\t")
    print(f"The sum of {bold_italic_start}{numbers}{bold_italic_end} is {bold_italic_start}{total}{bold_italic_end}")

if __name__ == '__main__':
    main()