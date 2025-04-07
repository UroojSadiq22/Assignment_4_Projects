# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0

import math

def pythagorean_theorem():
    print("This tool calculates the length of the hypotenuse of a right triangle using the Pythagorean theorem.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    ab: str = input("Enter the length of AB: ")
    ac: str = input("Enter the length of AC: ")
    
    ab: float = float(ab)
    ac: float = float(ac)
    
    bc: float = math.sqrt(ab**2 + ac**2)
    
    print("\t")
    print(f"The length of BC (the hypotenuse) is: {bold_italic_start}{bc}{bold_italic_end}")

if __name__ == '__main__':
    pythagorean_theorem()