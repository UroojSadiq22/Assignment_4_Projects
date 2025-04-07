# # Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# # Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# # What's your favorite animal? cow

# # My favorite animal is also cow!

def favorite_animal():
    print("This tool asks you for your favorite animal and responds with the same animal.")
    print("Please enter your favorite animal.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    animal: str = input("What's your favorite animal? ")
    print("\t")
    print(f"My favorite animal is also {bold_italic_start}{animal}{bold_italic_end}!")

if __name__ == '__main__':
    favorite_animal()
