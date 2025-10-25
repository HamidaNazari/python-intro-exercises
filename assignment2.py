"""
Assignment 2: Circle Circumference & Discount Calculator

Author: Hamida Nazari

-------------------------------------------------------------
PART 1: Circle Circumference Calculator
-------------------------------------------------------------
Description:
- Get the radius of a circle from the user.
- Calculate circumference using formula: circumference = 2 * π * radius.

Sample Inputs and Outputs:
--------------------------
Input: 5
Output: circumference of circle is: 31.41592653589793

Input: 15
Output: circumference of circle is: 94.24777960769379

Input: 100
Output: circumference of circle is: 628.3185307179587

# Code sample:
import math
r = float(input("Enter the radius of the circle "))
c = 2 * math.pi * r
print("circumference of circle is:", c)

-------------------------------------------------------------
PART 2: Discount Calculator for Items and Packs
-------------------------------------------------------------
Case A: Single Item (No Discount)
- User enters the cost price and discount percentage (usually 0).
- Sale price = cost price.

Example:
--------
enter cost price: 200
Enter discount percentage: 0
Discount is: 0.0
sale price is: 200.0

# Code sample:
Cost = float(input("enter cost price: "))
dis = float(input("Enter discount percentage: "))
discount = dis * Cost / 100
saleprice = Cost - discount
print("Discount is", discount)
print("sale price is", saleprice)

-------------------------------------------------------------
Case B: Combo Pack (2 Items, 10% Discount Each)
- User enters prices and discounts for two items.
- Sale price = sum of items after discount.

Example:
--------
enter cost price: 200
Enter discount percentage: 10
enter cost price: 400
Enter discount percentage: 10
Discount is: 20.0
Discount is: 40.0
sale price is: 540.0

# Code sample:
firstitemCost = float(input("enter cost price: "))
firstitemdis = float(input("Enter discount percentage: "))
discount1 = firstitemdis * firstitemCost / 100

seconditemCost = float(input("enter cost price: "))
seconditemdis = float(input("Enter discount percentage: "))
discount2 = seconditemdis * seconditemCost / 100

saleprice = (firstitemCost - discount1) + (seconditemCost - discount2)
print("Discount is", discount1)
print("Discount is", discount2)
print("sale price is", saleprice)

-------------------------------------------------------------
Case C: Gift Pack (3 Items, 25% Discount Each)
- User enters prices and discounts for three items.
- Sale price = sum of all after discount.

Example:
--------
enter cost price: 200
Enter discount percentage: 25
enter cost price: 400
Enter discount percentage: 25
enter cost price: 600
Enter discount percentage: 25
Discount is: 50.0
Discount is: 100.0
Discount is: 150.0
sale price is: 900.0

# Code sample:
firstitemCost = float(input("enter cost price: "))
firstitemdis = float(input("Enter discount percentage: "))
discount1 = firstitemdis * firstitemCost / 100

seconditemCost = float(input("enter cost price: "))
seconditemdis = float(input("Enter discount percentage: "))
discount2 = seconditemdis * seconditemCost / 100

thirditemCost = float(input("enter cost price: "))
thirditemdis = float(input("Enter discount percentage: "))
discount3 = thirditemdis * thirditemCost / 100

saleprice = (firstitemCost - discount1) + (seconditemCost - discount2) + (thirditemCost - discount3)
print("Discount is", discount1)
print("Discount is", discount2)
print("Discount is", discount3)
print("sale price is", saleprice)

-------------------------------------------------------------
All code written/tested as part of my Python learning journey. Feel free to review or give feedback!
"""

