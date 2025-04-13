def get_user_info():
    """Get user information and return it as a tuple."""
    print("This tool collects your information.")
    print("\t")

    f_name = input("Enter your first name: \033[94m")  # Set text color to blue
    print("\033[0m", end="")  # Reset text color to default

    l_name = input("Enter your last name: \033[94m")  # Set text color to blue
    print("\033[0m", end="")  # Reset text color to default

    email_address = input("Enter your email address: \033[94m")  # Set text color to blue
    print("\033[0m", end="")  # Reset text color to default

    return f_name, l_name, email_address  # Return the collected information as a tuple

def main():
    """Main function to get user information and display it."""
    user_info = get_user_info()  # Call the function to get user information

    print(f"Recieved the following information: {user_info}")  # Display the collected information

if __name__ == '__main__':
    main()  # Call the main function to execute the program