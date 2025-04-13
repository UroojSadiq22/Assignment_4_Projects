import time

def main():
    """Main function to print countdown and liftoff message."""
    print("Countdown to Liftoff!")
    print("\t")
    
    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i, end=' ', flush=True)
        time.sleep(0.4)  

    print("Liftoff!")

if __name__ == '__main__':
    main()