prompt: str = "What do you want?"
joke:str = "Here is a joke for you: Why did the scarecrow win an award? Because he was outstanding in his field!"
sorry:str = "Sorry, I only know how to tell jokes. Type 'joke' to hear one or 'exit' to quit."

def main():
    """Main function to interact with the user."""
    print("This tool tells you a joke.")
    print("\t")

    while True:
        user_input = input(prompt).strip().lower()

        if user_input == "joke":
            print(joke)
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print(sorry)

if __name__ == '__main__':
    main()