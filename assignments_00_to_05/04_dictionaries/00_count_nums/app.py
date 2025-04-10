def get_user_number():
    """Prompt the user for a number and return it."""
    user_numbers = []
    while True:
        number = input("Please enter a number (or 'enter' to finish): ")
        if number == '':
            break
        try:
            user_numbers.append(int(number))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return user_numbers

def count_nums(numbers):
    """Count the occurrences of each number in the list."""
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    return count_dict

def main():
    """Main function to get user input and count numbers."""
    print("This tool counts the occurrences of numbers you enter.")
    print("\t")
    
    # Get user numbers
    user_numbers = get_user_number()
    
    # Count occurrences of each number
    number_counts = count_nums(user_numbers)
    
    # Display the counts
    print("\t")
    print("Number Counts:")
    for number, count in number_counts.items():
        print(str(number) + " appears " + str(number_counts[number]) + " times.")

if __name__ == '__main__':
    main()