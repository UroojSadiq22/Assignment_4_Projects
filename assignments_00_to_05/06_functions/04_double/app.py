def double_num(number:int):
    return number * 2

def main():
    """Main function to get user input and double it."""
    print("This tool doubles the number you enter.")
    print("\t")
    
    user_input = int(input("Enter the number to double it: "))

    double_number = double_num(user_input)
    print(f"Double that is {double_number}")

if __name__ == '__main__':
    main()