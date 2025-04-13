def print_multiple(message: str, times: int) -> None:
    """Print a message multiple times."""
    for _ in range(times):
        print(message)

def main() -> None:
    """Main function to get user input and print it multiple times."""
    print("This tool prints the message you enter multiple times.")
    print("\t")

    user_input = input("Enter the message to print: \033[94m")  # Set text color to blue
    print("\033[0m", end="")  # Reset text color to default

    times = int(input("Enter the number of times to print it: "))

    print_multiple(user_input, times)

if __name__ == '__main__':
    main()