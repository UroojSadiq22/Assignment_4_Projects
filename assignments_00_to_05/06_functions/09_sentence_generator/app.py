def make_sentence(word:str , parts_of_speech:int):
    if parts_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them.")
    elif parts_of_speech == 1:
        print(f"It's so nice outside today, It makes me want to {word} all day.")
    elif parts_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Parts of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    print("This tool generates a sentence based on the word and part of speech you enter.")
    print("\t")
    
    user_input = input("Please type a noun, verb, or adjective: ")

    print("Is this a noun, verb, or adjective?")

    parts_of_speech = int(input("Type 0 for noun, 1 for verb, or 2 for adjective: "))

    make_sentence(user_input, parts_of_speech)

if __name__ == '__main__':  
    main()