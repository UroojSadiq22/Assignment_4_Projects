max_value = 1000

def main():
    """Main function to generate and display Fibonacci numbers."""
    print("This tool generates and displays Fibonacci numbers.")
    print("\t")
    
    # Initialize the first two Fibonacci numbers
    current_term, next_term = 0, 1
    
    # Generate and display Fibonacci numbers until the maximum value is reached
    while current_term < max_value:
        print(current_term)
        term_after_next = current_term + next_term
        current_term = next_term
        next_term = term_after_next

if __name__ == '__main__':
    main()
