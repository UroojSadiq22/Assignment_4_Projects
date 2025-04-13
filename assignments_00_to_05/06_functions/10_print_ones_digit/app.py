def print_ones_digit(number: int):
    ones_digit = abs(number) % 10  # Ensure the number is positive before getting the ones digit
    print(f"The ones digit of {number} is {ones_digit}.")

def main():
    """Main function to get user input and print its ones digit."""
    print("This tool finds the ones digit of the number you enter.")
    print("\t")
    
    user_input = int(input("Enter a number to find its ones digit: \033[94m"))
    print("\033[0m", end="")  # Reset text color to default


    print_ones_digit(user_input)

if __name__ == '__main__':
    main()