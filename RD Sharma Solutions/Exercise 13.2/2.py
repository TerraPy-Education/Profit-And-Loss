# Find the M.P. if
#   (i) S.P. = Rs 1222 and Discount = 6%
#   (ii) S.P. = Rs 495 and Discount = 1%

def findMP(selling_price, discount):
    marked_price = (100 * selling_price) / (100 - discount)
    return marked_price

print("M.P: ", findMP(1222, 6))
print("M.P: ", findMP(495, 1))
