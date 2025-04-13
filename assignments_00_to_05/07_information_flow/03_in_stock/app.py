def num_in_stock(fruits):
    if fruits == "Apple":
        return 5
    elif fruits == "Banana":
        return 10
    elif fruits == "Cherry":
        return 1000
    else :
        return 0

def main():
    print("This tool checks how many fruits are in stock.")
    print("\t")

    fruit = str(input("Enter the fruit name: "))

    stock = num_in_stock(fruit)

    if stock > 0:
        print(f"There are {stock} {fruit}(s) in stock.")
    else:
        print(f"There are no {fruit}s in stock.")

if __name__ == '__main__':
    main()