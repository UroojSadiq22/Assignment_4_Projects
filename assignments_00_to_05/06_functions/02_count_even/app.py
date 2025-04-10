def get_list_of_ints():
    """Prompt the user for a list of integers and return it."""
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


def main():
    """Main function to get user input and count even numbers."""
    print("This tool counts the number of even integers you enter.")
    print("\t")
    
    # Get user numbers
    user_numbers = get_list_of_ints()
    
    # Count even numbers
    count = 0  
    for num in user_numbers:  
        if num % 2 == 0: 
            count += 1  
    print(count) 
    
if __name__ == '__main__':
    main()



# def count_even(lst):
#     count = 0  
#     for num in lst:  
#         if num % 2 == 0: 
#             count += 1 

#     print(count) 

# def get_list_of_ints():
#     lst = []  
#     user_input = input("Enter an integer or press enter to stop: ") 
#     while user_input != "":  
#         lst.append(int(user_input))  
#         user_input = input("Enter an integer or press enter to stop: ") 

#     return lst

# def main():
#     lst = get_list_of_ints()
#     count_even(lst)


# if __name__ == '__main__':
#     main()