import random

def main():
    """Main function to play the 'Guess My Number' game."""
    print("Welcome to 'Guess My Number'!")
    print("\t")

    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    guess = int(input("Enter your guess (1-100): "))

    while guess != secret_number:
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        guess = int(input("Enter new guess (1-100): "))
    
    print(f"Congratulations! You guessed the number {secret_number} in {attempts + 1} attempts.")

if __name__ == '__main__':
    main()