affirmation: str = "I am capable of doing anything I put my mind to."

def main():
    """Main function to prompt for affirmation."""
    print("Please type the following affirmation:")
    print(affirmation)
    print("\t")

    user_input = input()

    while user_input != affirmation:
        print("Hmmm That was not the affirmation. Please type the following affirmation:")
        print(affirmation)
        print("\t")
        user_input = input()

    print("That's right! :)")

if __name__ == '__main__':
    main()
