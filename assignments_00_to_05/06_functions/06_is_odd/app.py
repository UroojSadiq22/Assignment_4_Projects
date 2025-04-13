def is_odd(number):
    remainder = number % 2
    return remainder == 1

def main():
    """Main function to get user input and check if it's odd."""
    print("This tool checks if the number you enter is odd.")
    print("\t")

    for i in range(10, 20):
        if is_odd(i):
            print(f"{i} is odd")
        else:
            print(f"{i} is even")

if __name__ == '__main__':
    main()