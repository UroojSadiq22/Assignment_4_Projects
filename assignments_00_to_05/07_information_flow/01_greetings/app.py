def greet(name: str) -> str:
    return f"Greetings, {name}!"

def main():
    print("This tool greets you with the name you enter.")
    print("\t")

    user_input = input("Enter your name: ")
    greeting = greet(user_input)
    print(greeting)

if __name__ == '__main__':
    main()