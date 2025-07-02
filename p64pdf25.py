mp=int(input("Enter a marked price="))
if mp <= 7000:
    print("Your discounted amount is",mp-mp/10)
elif 7000 < mp <= 10000:
    print("Your discounted amount is",mp-mp*0.15)
elif mp >= 10000:
    print("Your discounted amount is",mp-mp*0.2)
else:
    print("Enter a marked price")
