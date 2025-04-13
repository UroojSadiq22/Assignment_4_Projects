def access_element_from_list(lst: list, index: int) -> str:
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

def modify_element_in_list(lst: list, index: int, value: str):
    try:
        lst[index] = value
    except IndexError:
        print("Index out of range")

def slicing_list(lst: list, start: int, end: int):
    try:
        return lst[start:end]
    except IndexError:
        print("Index out of range")

def main():
    """Main function to demonstrate list operations."""
    print("\t")
    print("This tool allows you to access, modify, and slice a list.")
    print("\033[94m------------------------------\033[0m")
    print("Let's get started!")
    print("\t")
    
    my_list = ['apple', 'banana', 'grape', 'orange', 'pineapple']

    print("Original list:", my_list)
    print("\t")

    while True:

        print("Choose an operation: ")
        print("1. Access")
        print("2. Modify") 
        print("3. Slice")
        print("4. Exit")

        choice = int(input("Enter your choice: \033[94m"))
        print("\033[0m", end="")

        if choice == 1:
            index = int(input("Enter the index to access: \033[94m"))
            print("\033[0m", end="")
            result = access_element_from_list(my_list, index)
            print(f"Accessed element: \033[94m{result}\033[0m")

        elif choice == 2:
            index = int(input("Enter the index to modify: \033[94m"))
            print("\033[0m", end="")
            value = input("Enter the new value: \033[94m")
            print("\033[0m", end="")
            modify_element_in_list(my_list, index, value)
            print(f"Modified list: \033[94m{my_list}\033[0m")

        elif choice == 3:
            start = int(input("Enter the start index for slicing: \033[94m"))
            print("\033[0m", end="")
            end = int(input("Enter the end index for slicing: \033[94m"))
            print("\033[0m", end="")
            result = slicing_list(my_list, start, end)
            print(f"Sliced list: \033[94m{result}\033[0m")

        elif choice == 4:
            print("Exiting the program.")
            print("\t")
            print("\033[94m------------------------------\033[0m")
            print("Thank you for using the weight calculator!")
            print("Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        print("\t")
        repeat = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("\t")
            print("\033[94m------------------------------\033[0m")
            print("Thank you for using the weight calculator!")
            print("Have a great day!")
            break
        

if __name__ == '__main__':
    main()
