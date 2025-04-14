import random

def choose_word():
    words = ["python", "java", "kotlin", "javascript", "hangman", "programming"]
    return random.choice(words)

def display_hangman(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    print("Welcome to Hangman!")
    print("\t")
    
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print(display_hangman(word, guessed_letters))
        guess = input("\nGuess a letter: \033[94m").lower()
        print("\033[0m") 
        print("\t")

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have \033[94m{attempts}\033[0m attempts left.\n")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: \033[92m{word}\033[0m")
            break
    else:
        print("\t")
        print(f"Game over! The word was: \033[91m{word}\033[0m")

if __name__ == '__main__':
    main()