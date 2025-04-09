peturksbouipo_age:int = 16
stanlaur_age:int = 25
mayengua_age:int = 48

def main():
    """Main function to determine voting eligibility based on age."""
    print("This tool determines if you are eligible to vote in Peturksbouipo, Stanlaur and Mayengua.")
    print("\t")
    
    age: int = int(input("How old are you? "))
    
    if age >= peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
    else:
        print(f"You are not eligible to vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
    
    if age >= stanlaur_age:
        print(f"You can vote in Stanlaur where the voting age is {stanlaur_age}.")
    else:
        print(f"You are not eligible to vote in Stanlaur where the voting age is {stanlaur_age}.")

    if age >= mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
    else:
        print(f"You are not eligible to vote in Mayengua where the voting age is {mayengua_age}.")

if __name__ == '__main__':
    main()