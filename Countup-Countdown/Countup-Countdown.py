"""
Countup & Countdown Project
Author: Hamida Nazari
Description: 
This Python script demonstrates recursion using two simple functions:
1. countup(n) - counts up from a negative number to zero.
2. countdown(n) - counts down from a positive number to zero.

Both functions print each number and display "Blastoff!" when reaching zero.
"""

def countup(n):
    """Counts up from n to 0 recursively."""
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n + 1)

def countdown(n):
    """Counts down from n to 0 recursively."""
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


# --- Example Usage ---
if __name__ == "__main__":
    start_up = int(input("Enter a negative number to start countup: "))
    print("\nCountup:")
    countup(start_up)

    start_down = int(input("\nEnter a positive number to start countdown: "))
    print("\nCountdown:")
    countdown(start_down)
