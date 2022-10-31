# If the selling price of 18 chairs be equal to selling price of 16 chairs, find the gain or loss percent.

# Solution

# Step 1: Define the cost price and selling price of one chair
cost_price = 1 # Let the cost price of one chair be Rs 1
# CP of 16 chairs = 16
# SP of 16 chairs = 18
selling_price = 18/16 # SP of one chair = 16/18

# Step 2: Calculate the gain or loss
if cost_price < selling_price:
    gain = selling_price - cost_price
    gain_percent = (gain / cost_price) * 100
    gain_percent = round(gain_percent, 2)
    print("Gain percent = ", gain_percent, "%")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percent = (loss / cost_price) * 100
    loss_percent = round(loss_percent, 2)
    print("Loss percent = ", loss_percent, "%")

