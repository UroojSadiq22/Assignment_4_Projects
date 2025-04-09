def main():
    """Main function to determine if a year is a leap year."""
    print("This tool determines if a year is a leap year.")
    print("\t")
    
    year: int = int(input("Enter a year: "))
    
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == '__main__':
    main()