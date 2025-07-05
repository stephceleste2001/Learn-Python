# Retrieving user inputs
itemPrice = float(input("What is the price of the item? $"))
percentageDiscount = float(input("What is the percentage discount?"))

# Processing
reducedPrice = itemPrice * percentageDiscount / 100

# Generting the output
print("The reduced price is $" + str(reducedPrice))