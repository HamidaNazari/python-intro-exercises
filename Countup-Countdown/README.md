# Countup & Countdown Project

**Author:** Hamida Nazari  
**Language:** Python 3

---

## Overview

The **Countup & Countdown Project** demonstrates the concept of **recursion** in Python.  
It includes two simple functions:

1. Countup – counts up from a negative number to zero  
2. Countdown – counts down from a positive number to zero  

Both functions print each number in the sequence and display "Blastoff!" when reaching zero.

---

## Features

- Demonstrates **recursion** in Python  
- Handles **user input**  
- Provides **clear and reusable functions**  
- Console-based output for easy demonstration

---

## Countup Function

The Countup function:

- Recursively counts up from a negative number to `0`  
- Prints each number along the way  
- Displays "Blastoff!" when `0` is reached  

**Example usage:**

```python
def countup(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n + 1)

# Example call
countup(-3)
```

**Expected output:**

```text
-3
-2
-1
Blastoff!
```

---

## Countdown Function

The Countdown function:

- Recursively counts down from a positive number to `0`  
- Prints each number along the way  
- Displays "Blastoff!" when `0` is reached  

**Example usage:**

```python
def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

# Example call
countdown(5)
```

**Expected output:**

```text
5
4
3
2
1
Blastoff!
```

---

## How to Run

1. Clone the repository or download the `countup_countdown.py` file.  
2. Open a terminal and navigate to the folder containing the script.  
3. Run the script using Python 3:

```bash
python countup_countdown.py
```

4. Follow the prompts:

- Enter a negative number to start the countup function  
- Enter a positive number to start the countdown function

---

## Example Program Run

```text
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
```

---

## Screenshot

![Example Output](./screenshot.png)  

---

## Learning Points

- Understanding **recursion** in Python  
- Using **conditional statements** (`if-else`)  
- Handling **user input**  
- Writing **clear and reusable functions**  
- Practicing **console output formatting**

---

## License

This project is **open-source** and free to use.  
Feel free to modify and share for educational purposes.
