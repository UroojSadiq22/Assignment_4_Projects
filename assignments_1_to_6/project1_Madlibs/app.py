
def madlib(name, color, animal, place, food):
    """Create a mad lib using the provided words."""
    return (
        f"One sunny day, \033[92m{name}\033[0m decided to visit \033[92m{place}\033[0m. "
        f"Upon arriving, they were amazed by the sight of a \033[92m{color}\033[0m \033[92m{animal}\033[0m "
        f"playing near a sparkling stream. Feeling adventurous, \033[92m{name}\033[0m followed the \033[92m{animal}\033[0m "
        f"and discovered a hidden grove filled with delicious \033[92m{food}\033[0m. "
        f"It was a magical day that \033[92m{name}\033[0m would never forget!"
    )

def main():
    """Main function to get user input and create a mad lib."""
    print("This tool creates a mad lib using the words you enter.")
    print("\t")

    name = input("Enter a name: \033[94m") 
    print("\033[0m", end="") 

    color = input("Enter a color: \033[94m") 
    print("\033[0m", end="") 

    animal = input("Enter an animal: \033[94m") 
    print("\033[0m", end="") 

    place = input("Enter a place: \033[94m") 
    print("\033[0m", end="") 

    food = input("Enter a food: \033[94m") 
    print("\033[0m", end="") 

    result = madlib(name, color, animal, place, food) 
    print(result) 

    print("\t")
    print("Thank you for using the mad lib tool!")
    

if __name__ == '__main__':
    main()  # Call the main function to execute the program