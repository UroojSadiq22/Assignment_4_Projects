# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

def triangle_perimeter():
    print("This tool calculates the perimeter of a triangle.")
    print("Please enter the lengths of each side of the triangle.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    side1: str = input("What is the length of side 1? ")
    side2: str = input("What is the length of side 2? ")
    side3: str = input("What is the length of side 3? ")
    
    side1: float = float(side1)
    side2: float = float(side2)
    side3: float = float(side3)
    
    perimeter: float = side1 + side2 + side3
    
    print("\t")
    print(f"The perimeter of the triangle is {bold_italic_start}{perimeter} units{bold_italic_end}")

if __name__ == '__main__':
    triangle_perimeter()