min_hight: int = 50

def main():
    """Main function to determine if a person is tall enough to ride."""
    print("This tool determines if you are tall enough to ride.")
    print("\t")
    
    height: float = float(input("Enter your height in cm: "))
    
    if height >= min_hight:
        print("You are tall enough to ride!")
    else:
        print("You are not tall enough to ride, but may be next year.")
    
if __name__ == '__main__':
    main()