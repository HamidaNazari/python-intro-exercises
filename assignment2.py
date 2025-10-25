"""
Assignment 2 — Circle Circumference & Discount Calculator

Author: Hamida Nazari

------------------------------------------------------------
Part 1: Circle Circumference Calculator
------------------------------------------------------------

Description:
Calculates the circumference of a circle based on user-provided radius, using the formula:

    circumference = 2 * π * radius

Sample Inputs & Outputs:
------------------------
Enter the radius of the circle 5
circumference of circle is: 31.41592653589793

Enter the radius of the circle 15
circumference of circle is: 94.24777960769379

Enter the radius of the circle 100
circumference of circle is: 628.3185307179587

------------------------------------------------------------
Part 2: Sale Price & Discount Calculator
------------------------------------------------------------

Description:
Calculates discounted sale prices for items, combos and gift packs. Different calculations for:
- Individual items (no discount)
- Combo packs (two items, 10% discount each)
- Gift packs (three items, 25% discount each)

A. Individual Item (No Discount)
   Input:
       Cost = float(input("enter cost price: "))
       dis = float(input("Enter discount percentage: "))
       discount = dis * Cost / 100
       saleprice = Cost - discount
   Output Example:
       enter cost price: 200
       Enter discount percentage: 0
       Discount is  0.0
       sale price is  200.0

B. Combo Pack (2 items, 10% discount)
   Input:
       [input for two items and discounts]
   Output Example:
       enter cost price: 200
       Enter discount percentage: 10
       enter cost price: 400
       Enter discount percentage: 10
       Discount is  20.0
       Discount is  40.0
       sale price is  540.0

C. Gift Pack (3 items, 25% discount)
   Input:
       [input for three items and discounts]
   Output Example:
       enter cost price: 200
       Enter discount percentage: 25
       enter cost price: 400
       Enter discount percentage: 25
       enter cost price: 600
       Enter discount percentage: 25
       Discount is  50.0
       Discount is  100.0
       Discount is  150.0
       sale price is  900.0

------------------------------------------------------------

# All scripts and logic written and tested independently as part of Python learning practice.
"""
