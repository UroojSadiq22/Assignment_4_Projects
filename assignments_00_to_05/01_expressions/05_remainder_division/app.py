# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

def remainder_division():
    print("This tool performs division and calculates the remainder.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    numerator: str = input("Please enter an integer to be divided: ")
    denominator: str = input("Please enter an integer to divide by: ")
    
    numerator: int = int(numerator)
    denominator: int = int(denominator)
    
    quotient: int = numerator // denominator
    remainder: int = numerator % denominator
    
    print("\t")
    print(f"The result of this division is {bold_italic_start}{quotient}{bold_italic_end} with a remainder of {bold_italic_start}{remainder}{bold_italic_end}")

if __name__ == '__main__':
    remainder_division()