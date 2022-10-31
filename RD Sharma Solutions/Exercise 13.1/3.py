# A boy buys 9 apples for Rs 9.60 and sells them at 11 for Rs 12. Find his gain or loss percent.

# Solution

# Step 1: Define the cost price and selling price of one apple
cost_price = 9.60/9 # 9 apples cost Rs 9.60
selling_price = 12/11 # 11 apples cost Rs 12

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