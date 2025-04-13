
def guess_number():
    """User guesses a number between 1 and 100."""

    lower_bound = 1
    upper_bound = 100

    print("Welcome to 'Guess My Number'!")
    print("\t")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print("Try to guess it!")
    print("\t")

    input("Press Enter to start the game...")

    guess = 0

    while True:
        guess = (lower_bound + upper_bound) // 2
        print(f"Is your number {guess}?")

        response = input("Enter 'h' if your number is higher, 'l' if it's lower, or 'c' if I guessed it right: ").lower()
        print("\t")

        if response == 'h':
            lower_bound = guess + 1
        elif response == 'l':
            upper_bound = guess - 1
        elif response == 'c':
            print(f"Yay! I guessed your number {guess} correctly.")
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
            print("\t")
            continue
    
    print("\t")
    print("\033[94m----------------------\033[0m")  # Blue color for the separator
    print("Thank you for playing!")

if __name__ == '__main__':
    guess_number()