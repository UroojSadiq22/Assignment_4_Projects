# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

def square_number():
    print("This tool calculates the square of a number.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    number: str = input("Type a number to see its square: ")
    number: float = float(number)
    
    squared: float = number * number
    
    print("\t")
    print(f"{number}{bold_italic_start} squared is {squared}{bold_italic_end}")

if __name__ == '__main__':
    square_number()
