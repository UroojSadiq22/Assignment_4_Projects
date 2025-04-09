# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program

def shorten(lst: list) -> None:
    """Shortens the list to a maximum length of MAX_LENGTH."""
    MAX_LENGTH: int = 3 
    print("\t")
    
    # Check if the list is longer than MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  
        print(f"Removed item: {removed_item}")  
    
    print("\t")
    print(f"List after shortening: {lst}")  

def main() -> None:
    """Main function to demonstrate the shorten function."""
    print("This tool shortens a list to a maximum length of 3.")
    print("\t")
    
    lst: list = []
    while True:
        element: str = input("Enter an element (or 'done' to finish): ")
        if element.lower() == 'done':
            break
        lst.append(element)
    
    print("\t")
    print(f"Original list: {lst}") 
    shorten(lst) 

if __name__ == '__main__':
    main() 