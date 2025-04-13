def main():
    """Main function to double numbers from 0 to 19."""
    print("This tool doubles numbers from 0 to 19.")
    print("\t")
    
    user_input = int(input("Please enter a number (or 'enter' to finish): "))
    current_value = user_input

    while current_value < 100:
        current_value = current_value * 2
        print(current_value)

if __name__ == '__main__':
    main()
       