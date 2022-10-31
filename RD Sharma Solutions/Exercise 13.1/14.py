# A defective briefcase costing Rs 800 is being sold at a loss of 8%. If the price is further reduced by 5%, find its selling price.
from sympy.abc import X
from sympy import Eq
import sympy

# Solution

# Step 1: Define the cost price of the book
cp = 800
sp = cp * (100-8)/100

sp2 = sp * (100-5)/100

# Step 3: Print the result
print("Selling price = Rs", round(sp2, 2))