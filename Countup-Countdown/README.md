# Countup & Countdown Project

**Author:** Hamida Nazari  
**Language:** Python 3  

---

## Overview

This project demonstrates **recursion** using two simple Python functions in Python 3.  
The program shows how recursion can be used to **count up from a negative number** or **count down from a positive number** to zero.

---

## Countup Function

The **Countup** function:

- Recursively counts up from a negative number to 0  
- Prints each number along the way  
- Displays `"Blastoff!"` when zero is reached

**Example usage:**

```python
def countup(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n + 1)

countup(-3)
Expected output:

diff
-3
-2
-1
Blastoff!

---

**Countdown Function**

The Countdown function:

Recursively counts down from a positive number to 0

Prints each number along the way

Displays "Blastoff!" when zero is reached

---

**##** **Example usage:**

def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
Expected output:

5
4
3
2
1
Blastoff!

---

**How to Run**

Clone the repository or download the code

Open a terminal and navigate to the folder containing countup_countdown.py

Run the script:

python countup_countdown.py
Enter the starting numbers as prompted:

A negative number for countup

A positive number for countdown

---

**Example Output**

Enter a negative number to start countup: -3

Countup:
-3
-2
-1
Blastoff!

Enter a positive number to start countdown: 5

Countdown:
5
4
3
2
1
Blastoff!

---


**Learning Points**

Understanding recursion in Python

Using conditional statements (if-else)

Handling user input

Writing clear and reusable functions

---

**Screenshots**
Here is an example of the program output:


---


**Feedback**
All code written and tested by myself as part of my Python learning journey.
Feel free to review, ask questions, or provide feedback!

