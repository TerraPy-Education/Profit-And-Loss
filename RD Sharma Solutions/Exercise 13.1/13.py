from sympy.abc import X
from sympy import Eq
import sympy

#  By selling a book for Rs 258, a bookseller gains 20%. For how much should he sell it to gain 30%?

# Solution

# Step 1: Define the selling price of the book
sp = 258
# SP = (100+20)/100 * CP
# let CP be X
cp = (100+20)/100 * X

sp2 = sp * (100+30)/100

# Step 2: Solve for X
equation = Eq(sp2, cp)
x = sympy.solve(equation)

# Step 3: Print the result
print("Cost price = Rs", round(x[0], 2))

