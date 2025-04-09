# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def get_first_element(lst: list) -> None:
    """Prints the first element of the list."""
    if lst:
        print(f"The first element is: {lst[0]}")
    else:
        print("The list is empty.")

def main():
    """Main function to demonstrate the get_first_element function."""
    print("This tool prints the first element of a list.")
    print("\t")
    
    # Prompt user to input the list one element at a time
    lst: list = []
    while True:
        element: str = input("Enter an element (or 'done' to finish): ")
        if element.lower() == 'done':
            break
        lst.append(element)
    
    print("\t")
    get_first_element(lst)

if __name__ == '__main__':
    main()