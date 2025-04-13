import random

rounds: int = 5

def main():
    """Main function to play a guessing game."""
    print("Welcome to the High and Low Game!")
    print("\033[94m------------------------------\033[0m")
    print("Try to guess the number I'm thinking of between 1 and 100.")
    print("You have 5 attempts to guess the number.")

    score: int = 0

    for i in range(rounds):
        print("\t")
        print("------------------------------")
        print(f"Attempt {i + 1}/{rounds}:")
        print("\t") 

        computer_number: int = random.randint(1, 100)
        guess: int = random.randint(1, 100)

        print(f"You guessed:\033[94m {guess} \033[0m")

        choice: str = input("Do you think your number is higher or lower than the computer's number? ( higher / lower ): \033[94m").strip().lower()
        print("\033[0m", end="")

        if choice == "higher" and guess > computer_number:
            print(f"Your answer is correct! The computer's number was \033[94m{computer_number}\033[0m.")
            score += 1
        else:
            print(f"Aww, your answer is wrong! The computer's number was \033[94m{computer_number}\033[0m.")

    print("\t")        
    print(f"Your current score is: \033[94m{score}\033[0m.")

    if score == rounds:
        print("Wow! You guessed all the numbers correctly!")
    elif score >= rounds / 2:
        print("Good job!")
    else:
        print("Better luck next time!")

    print("\t")    
    print("\033[94m------------------------------\033[0m")
    print("Thank you for playing!")
    print("Goodbye!")

if __name__ == '__main__':
    main()