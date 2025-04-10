def read_phone_numbers():
    phone_book = {}
    while True:
        name = input("Enter name (or 'enter' to finish): ")
        if name == '':
            break
        number = input("Enter phone number: ")
        phone_book[name] = number
    return phone_book

def print_notebook(phone_book):
    print("\t")
    print("Phone Book:")
    for name, number in phone_book.items():
        print(f"{name}: {number}")
    print("\t")

def lookup_phonebook(phone_book):
    while True:
        name = input("Enter name to look up (or 'enter' to finish): ")
        if name == '':
            break
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print(f"{name} not found in the phone book.")
    print("\t")

def main():
    """Main function to read, print, and look up phone numbers."""
    print("This tool manages a phone book.")
    print("\t")
    
    # Read phone numbers into the phone book
    phone_book = read_phone_numbers()
    
    # Print the phone book
    print_notebook(phone_book)
    
    # Look up names in the phone book
    lookup_phonebook(phone_book)

if __name__ == '__main__':
    main()