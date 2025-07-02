print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")

op=int(input("Enter option => "))

if op==1:
    a1=float(input("Enter first number for addition=>"))
    a2=float(input("Enter second number for addition=>"))
    print("The addition is=",a1+a2)

elif op==2:
    s1=float(input("Enter first number for subtraction=>"))
    s2=float(input("Enter second number for subtraction=>"))
    print("The subtraction is=",s1-s2)

elif op==3:
    m1=float(input("Enter first number for multiplication=>"))
    m2=float(input("Enter second number for multiplication"))
    print("The multiplication is=",m1*m2)
elif op==4:
    d1=float(input("Enter first number for divisio n=>"))
    d2=float(input("Enter second number for division=>"))
    print("The division is=",d1/d2)

else:
    print("Enter option from 1 to 4")



