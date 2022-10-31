import sympy
from sympy.abc import X

# Ramesh bought two boxes for Rs 1300. He sold one box at a profit of 20% and the other box at a loss of 12%. If the selling price of both boxes is the same, find the cost price of each box.

# Solution

# So let us consider cost price of one box be Rs x
# Cost price of other box = Rs 1300 – x
# Selling price of first box = x * (100+20)/100
# Selling price of second box = (1300 – x) * (100-12)/100

# Selling price of first box = Selling price of second box

# x * (100+20)/100 = (1300 – x) * (100-12)/100

# Step 1: Solving for x
equation = X * (100+20)/100 - (1300 - X) * (100-12)/100
x = sympy.solve(equation)

# Step 2: Print the result
print("Cost price of one box = Rs", x[0])
print("Cost price of other box = Rs", 1300 - x[0])

