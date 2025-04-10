def average(a: float, b: float) -> float:
    return (a + b) / 2

def main():
    """Main function to calculate the average of two numbers."""
    print("This tool calculates the average of two numbers.")
    print("\t")
    
    user_input_a = float(input("Please enter the first number: "))
    user_input_b = float(input("Please enter the second number: "))

    result = average(user_input_a, user_input_b)
    print(f"The average of {user_input_a} and {user_input_b} is {result}.")

if __name__ == '__main__':
    main()