# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst: list) -> None:
    """Prints the last element of the list."""
    if lst:
        print(f"The last element is: {lst[-1]}")
    else:
        print("The list is empty.")

def main():
    """Main function to demonstrate the get_last_element function."""
    print("This tool prints the last element of a list.")
    print("\t")
    
    # Prompt user to input the list one element at a time
    lst: list = []
    while True:
        element: str = input("Enter an element (or 'done' to finish): ")
        if element.lower() == 'done':
            break
        lst.append(element)
    
    print("\t")
    get_last_element(lst)

if __name__ == '__main__':
    main()