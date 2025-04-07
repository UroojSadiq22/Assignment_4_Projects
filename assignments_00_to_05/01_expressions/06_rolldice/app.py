# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Die 1: {die1}, Die 2: {die2}, Sum: {die1 + die2}")
    print("\t")

def main():
    print("Rolling the dice three times...")
    roll_dice()
    roll_dice()
    roll_dice()
    print("Done rolling the dice.")

if __name__ == '__main__':
    main()