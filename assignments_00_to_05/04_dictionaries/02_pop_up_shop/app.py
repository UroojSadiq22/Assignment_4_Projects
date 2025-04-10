def main():
    """Main function to manage a pop-up shop."""
    print("Welcome to the Pop-Up Shop!")
    print("\t")

    fruits = {
        "apple": 0.5,
        "banana": 0.25,
        "orange": 0.75,
        "grape": 1.0,
        "kiwi": 1.5
    }

    total_cost = 0.0

    for fruit, price in fruits.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit}s(${price}) would you like to buy? "))
                if quantity < 0:
                    print("Quantity must be a positive integer. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
                
        item_total = quantity * price
        total_cost += item_total
    
    print("Your total is $" + str(total_cost))

if __name__ == '__main__':
    main()