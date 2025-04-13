import random

def rock_paper_scissors():
    """Play Rock, Paper, Scissors."""
    print("Welcome to 'Rock, Paper, Scissors'!")
    print("\t")
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("\t")

    user_choice = int(input("Enter your choice (1-3): "))
    computer_choice = random.randint(1, 3)

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("You lose!")

if __name__ == '__main__':
    rock_paper_scissors()