def print_divisors(number:int):
    """Print all divisors of a given number."""
    print(f"Divisors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

def main():
    """Main function to get user input and print its divisors."""
    print("This tool prints all divisors of the number you enter.")
    print("\t")

    user_input = int(input("Enter the number to find its divisors: \033[94m"))  
    print("\033[0m", end="")  # Reset text color to default# Set text color to blue

    print_divisors(user_input)

if __name__ == '__main__':
    main()