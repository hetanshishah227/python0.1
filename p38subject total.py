math=int(input("Enter math marks "))
chem=int(input("Enter chem marks "))
phy=int(input("Enter physics marks "))
subtotal=math+phy+chem
if 0 < subtotal < 50:
    print("C grade")
elif 50 < subtotal < 80:
    print("B grade")
else:
    print("A grade")
