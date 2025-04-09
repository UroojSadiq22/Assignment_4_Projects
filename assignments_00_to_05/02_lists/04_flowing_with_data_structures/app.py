# This program demonstrates how to add three copies of a user-provided message to a list.

def add_three_copies(data: str, lst: list) -> None:
    """Adds three copies of data to the list."""
    for i in range(3):
        lst.append(data)

def main():
    """Main function to demonstrate the add_three_copies function."""
    print("This tool adds three copies of a message to a list.")
    print("\t")
 
    data: str = input("Enter a message to copy: ")
    
    lst: list = []
    
    print("\t")
    print(f"List before: {lst}")
    
    add_three_copies(data, lst)
    
    print("\t")
    print(f"List after: {lst}")

if __name__ == '__main__':
    main()