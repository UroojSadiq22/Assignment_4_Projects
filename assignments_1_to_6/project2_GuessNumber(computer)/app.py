# you will build a guessing game where the computer has to guess the correct number. You will work with Python's random module, build functions, work with while loops and conditionals, and get user input.

def guess_number():
    """Computer guesses a number between 1 and 100."""
    import random

    print("Welcome to 'Guess My Number'!")
    print("\t")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print("\t")

    secret_number = random.randint(1, 100)

    attempts = 0

    guess = int(input("Enter your guess (1-100): "))
    print("\t")

    while guess != secret_number:
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("That's not a valid guess!")
        
        guess = int(input("Enter new guess (1-100): "))
    
    print("\t")
    print("\033[94m----------------------\033[0m")  # Blue color for the separator
    print(f"Congratulations! You guessed the number {secret_number} in {attempts + 1} attempts.")

guess_number()