# A shopkeeper allows his customers 10% off on the marked price of goods and still gets a profit of 25%. What is the actual cost to him of an article marked Rs. 250?

# Solution

# Step 1: Define the marked price, discount and profit
marked_price = 250
discount_percent = 10
profit = 25

# Step 2: Calculate the cost price
discount = marked_price * discount_percent / 100
selling_price = marked_price - discount
cost_price = 100 / (100 + discount) * selling_price 

# Step 3: Print the result
print("Cost price = Rs", cost_price)
