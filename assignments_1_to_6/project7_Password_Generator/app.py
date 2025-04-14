import random

def generate_password(length):
    """Generate a random password."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated password: \033[92m{password}\033[0m")

def main():
    """Main function to generate a password."""
    print("Welcome to the Password Generator!")
    print("\t")
    
    while True:
        while True:
            user_input = input("Enter the desired password length (minimum 12): \033[94m") or "12"
            print("\033[0m", end="")
            print("\t")

            if not user_input.isdigit():
                print("\033[91mInvalid input. Please enter a number.\033[0m")
                continue

            length = int(user_input)

            if length < 12:
                print("\033[91mPassword length should be at least 12 characters for security.\033[0m\n")
            else:
                generate_password(length)
                break

        repeat = input("\nDo you want to generate another password? (yes/no): \033[94m").lower()
        print("\033[0m", end="")

        if repeat != "yes":
            print("\t")
            print("\033[94m-----------------------\033[0m")
            print("Thank you for using the Password Generator! Stay secure!\n")
            break
    

if __name__ == '__main__':
    main()

