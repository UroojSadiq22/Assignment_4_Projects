import random

def main():
    """Main function to generate and display random numbers."""
    print("This tool generates and displays random numbers.")
    print("\t")
    
    # Generate and display 10 random numbers between 1 and 100
    for i in range(10):
        print(f"Random number {i+1}: {random.randint(1, 100)}")

if __name__ == '__main__':
    main()