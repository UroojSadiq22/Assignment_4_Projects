# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

def fahrenheit_to_celsius():
    print("This tool converts Fahrenheit to Celsius.")
    print("Please enter a temperature in Fahrenheit.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    fahrenheit: str = input("Enter temperature in Fahrenheit: ")
    fahrenheit: float = float(fahrenheit)
    
    celsius: float = (fahrenheit - 32) * 5.0 / 9.0
    
    print("\t")
    print(f"Temperature: {fahrenheit}{bold_italic_start}F{bold_italic_end} = {celsius}{bold_italic_start}C{bold_italic_end}")

if __name__ == '__main__':
    fahrenheit_to_celsius()