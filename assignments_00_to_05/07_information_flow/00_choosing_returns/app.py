adult_age: int = 18

def is_adult(age: int) -> bool:
    if age >= adult_age:
        return True

    return False

def main():
    print("This tool checks if you are an adult based on the age you enter.")
    print("\t")

    user_age = int(input("Enter your age: "))

    print(is_adult(user_age))

if __name__ == '__main__':
    main()