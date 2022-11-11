# Find the discount in percent when
#   (i) M.P. = Rs. 900 and S.P. = Rs. 873
#   (ii) M.P. = Rs. 500 and S.P. = Rs. 425

# Solution

def findDiscount(marked_price, selling_price):
    discount = (marked_price - selling_price) * 100 / marked_price
    return discount

print("Discount: ", findDiscount(900, 873))
print("Discount: ", findDiscount(500, 425))