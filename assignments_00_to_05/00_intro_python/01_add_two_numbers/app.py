def sum():
    print("This tool reads two numbers and adds them together.")
    print("Please enter two numbers to add them together.")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The total is " + str(total) + ".")

if __name__ == '__main__':
    sum()