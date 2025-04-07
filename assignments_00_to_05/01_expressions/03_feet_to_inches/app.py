# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def feet_to_inches():
    print("This tool converts feet to inches.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    feet: str = input("Enter distance in feet: ")
    feet: float = float(feet)
    
    inches: float = feet * 12
    
    print("\t")
    print(f"Distance: {feet}{bold_italic_start}ft{bold_italic_end} = {inches}{bold_italic_start}in{bold_italic_end}")

if __name__ == '__main__':
    feet_to_inches()
