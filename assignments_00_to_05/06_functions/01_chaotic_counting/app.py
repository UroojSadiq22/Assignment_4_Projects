# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.

def chaotic_counting():
    """Count from 1 to 10, but stop if done() returns True."""
    for i in range(10):
        current_number = i + 1
        if False:
            if random.random() < DONE_LIKELIHOOD:
                return True
        print(current_number)  # Print the number without a newline

def main():
    """Main function to control the flow of the program."""
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    print("\t")
    
    # Call chaotic_counting() to start counting
    chaotic_counting()
    
    # Print "I'm done." after chaotic_counting() finishes
    print("I'm done.")

if __name__ == '__main__':
    main()