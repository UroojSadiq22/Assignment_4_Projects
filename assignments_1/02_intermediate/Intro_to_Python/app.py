import math

mercury_gravity = 0.377
venus_gravity = 0.903
earth_gravity = 1.0
mars_gravity = 0.378
jupiter_gravity = 2.528
saturn_gravity = 1.065
uranus_gravity = 0.886
neptune_gravity = 1.14
pluto_gravity = 0.063

gravity_constant = ""

planet_name = {
    "ME": "Mercury",
    "V": "Venus",
    "MA": "Mars",
    "J": "Jupiter",
    "S": "Saturn",
    "U": "Uranus",
    "N": "Neptune",
    "P": "Pluto"
    }

def main():
    """Main function to calculate weight on different planets."""
    print("\t")
    print("This tool calculates your weight on different planets.")
    print("\033[94m------------------------------\033[0m")
    print("Let's get started!")
    print("\t")

    earth_weight = float(input("Please enter your weight on Earth (in kg): "))
    print("\t")

    current_weight = earth_weight

    while True:
        planet = input("Please enter the first letter of the planet (Me for Mercury, V for Venus, Ma for Mars, J for Jupiter, S for Saturn, U for Uranus, N for Neptune, P for Pluto): \033[94m").upper()
        print("\033[0m", end="")  # Reset text color to default
    
        
        if planet in planet_name:
            gravity_constant = globals()[f"{planet_name[planet].lower()}_gravity"]
        else:
            print("Invalid planet selection. Please try again.")
            continue
            return

        planetry_weight = earth_weight * gravity_constant
        planetry_weight = round(planetry_weight, 2)

        print("\t")
        print("\033[94m------------------------------\033[0m")
        

        print("\t")
        print(f"Your weight on {planet_name[planet]} is approximately {planetry_weight} kg.")

        print("\t")
        repeat = input("Would you like to calculate your weight on another planet? (yes/no): \033[94m").lower()
        print("\033[0m", end="")  # Reset text color to default

        if repeat == "yes":
            print("\t")
            change_weight = input("Do you want to use your existing weight or enter a new one? (e for existing / n for new): \033[94m").lower()
            print("\033[0m", end="")

            if change_weight == "n":
                print("\t")
                current_weight = float(input("Please enter your new weight on Earth (in kg): "))
        else:
            break

    print("\t")
    print("\033[94m------------------------------\033[0m")
    print("Thank you for using the weight calculator!")
    print("Have a great day!")

if __name__ == '__main__':
    main()