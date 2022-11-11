#  Find the S.P. if
#    (i) M.P. = Rs 1300 and Discount = 10%
#    (ii) M.P. = Rs 500 and Discount = 15%

# Solution

# Now that we have a problem with two parts, the convenient way would be to create a function out of the solution.

def findSP(marked_price, discount):
    selling_price = marked_price - (marked_price * discount / 100)
    return selling_price

print("S.P: ", findSP(1300, 10))
print("S.P: ", findSP(500, 15))
