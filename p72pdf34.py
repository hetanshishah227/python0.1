print("Press 1 for Battery based toys")
print("Press 2 for Key based toys")
print("Press 3 for Electrical based toys")

op=int(input("Enter your option=>"))

if op==1:
 o=int(input("Enter your order value=>"))
 if o > 1000:
  print("Congratulations!You've received a discount of 10%")
  print("Amount to pay is=>",o-o*0.1)
 else:
  print("Amount to pay is=>",o)

elif op==2:
 o = int(input("Enter your order value=>"))
 if o > 100:
    print("Congratulations!You've received a discount of 10%")
    print("Amount to pay is=>",o-o*0.05)
 else:
  print("Amount to pay is=>", o)

elif op == 3:
 o = int(input("Enter your order value=>"))
 if o > 500:
    print("Congratulations!You've received a discount of 10%")
    print("Amount to pay is=>", o - o * 0.1)
 else:
  print("Amount to pay is=>",o)

else:
    print("Enter 1,2 or 3")






