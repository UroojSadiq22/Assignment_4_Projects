def get_name():
    
    name = input("Please enter your name: ")
    return name

def main():
    """Main function to get user name."""
    print("This tool gets your name.")
    print("\t")
    
    user_name = get_name()
    
    print(f"Hello, {user_name}!")

if __name__ == '__main__':
    main()