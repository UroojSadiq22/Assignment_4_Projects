def subtract_seven(number):
    """Subtract 7 from the given number and print the result."""
    result = number - 7
    print(f"The result of subtracting 7 from {number} is {result}.")

def main():
    """Main function to get user input and subtract 7 from it."""
    print("This tool subtracts 7 from the number you enter.")
    print("\t")

    user_input = int(input("Enter a number to subtract 7 from: \033[94m")) 
    print("\033[0m", end="")  

    subtract_seven(user_input)

if __name__ == '__main__':
    main() 