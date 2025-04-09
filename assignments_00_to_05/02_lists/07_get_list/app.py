# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def get_list() -> list:
    """Prompts the user to enter values and returns a list of those values."""
    lst: list = []
    while True:
        value: str = input("Enter a value (or press Enter to finish): ")
        if value == "":
            break
        lst.append(value)
    return lst

def main() -> None:
    """Main function to demonstrate the get_list function."""
    print("This tool collects values into a list.")
    print("\t")
    
    lst: list = get_list()
    
    print("\t")
    print(f"Here's the list: {lst}")

if __name__ == '__main__':
    main()