# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Sum of the two dice: {die1 + die2}")
    print("\t")

        
def main():
    dice1:int = 6
    print(f"Value of Dice 1 is {dice1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"Value of Dice 1 is {dice1}")  # This will still work because dice1 is in the global scope

if __name__ == '__main__':
    main()
