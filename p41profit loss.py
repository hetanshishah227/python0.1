cp=float(input("Enter cost price of mobile"))
sp=float(input("Enter selling price of mobile"))
if sp>cp:
    print(" It is profit and profit amount is ",sp-cp)
else:
    print("It is loss and loss amount is ",cp-sp)
    