# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

sentence_start: str = "Code in Place is fun. I learned to program and used Python to make my"

def tiny_mad_lib():
    print("This tool creates a fun sentence using your words.")
    print("\t")
    
    # ANSI escape codes for bold and italic formatting
    bold_italic_start = "\033[1m\033[3m"
    bold_italic_end = "\033[0m"
    
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")
    
    print("\t")
    print(f"{sentence_start} {bold_italic_start}{adjective}{bold_italic_end} {bold_italic_start}{noun}{bold_italic_end} {bold_italic_start}{verb}{bold_italic_end}")

if __name__ == '__main__':
    tiny_mad_lib()