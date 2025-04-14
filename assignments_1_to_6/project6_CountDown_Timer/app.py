import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
        if seconds == 0:
            print("\033[92mTime's up!\033[0m")
            print("\nOptions: [1] Restart [2] Reset [3] Finish")
            choice = input("Enter your choice: ")
            if choice == '1':
                seconds = int(input("Enter the number of seconds to count down from: "))
            elif choice == '3':  # Finish
                print("\t")
                print("\033[94m--------------------\033[0m")
                print("Exiting countdown.")
                print("Thank you for using the countdown timer!")
                break
            else: 
                print("\t")
                print("\033[94m--------------------\033[0m")
                print("Invalid choice. Exiting countdown.")
                break

def main():
    print("This tool counts down from the number of seconds you enter.")
    print("\t")

    user_input = int(input("Enter the number of seconds to count down from: \033[94m"))
    print("\033[0m", end="")

    countdown_timer(user_input)

if __name__ == '__main__':
    main()
    