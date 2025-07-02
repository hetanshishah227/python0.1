clsheld=int(input("Enter the number of classes held this term="))
clsattend=int(input("Enter the number of classes attended this term="))
print("Your attendance this term is=",clsattend*100/clsheld,"%")

if clsattend*100/clsheld > 75:
    print("You are eligible to sit in the examination.")
else:
    print("Sorry, You aren't eligible to give this exam.")
