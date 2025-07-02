print("Press + for addition")
print("Press - for subtraction")
print("Press x for multiplication")
print("Press / for division")

op=input("Enter option => ")

if op=="+":
    a1=float(input("Enter first number for + =>"))
    a2=float(input("Enter second number for + =>"))
    print("The addition is=",a1+a2)

elif op=="-":
    s1=float(input("Enter first number for - =>"))
    s2=float(input("Enter second number for - =>"))
    print("The subtraction is=",s1-s2)

elif op=="x":
    m1=float(input("Enter first number for x =>"))
    m2=float(input("Enter second number for x =>"))
    print("The multiplication is=",m1*m2)
elif op=="/":
    d1=float(input("Enter first number for / =>"))
    d2=float(input("Enter second number for / =>"))
    print("The division is=",d1/d2)

else:
    print("Enter option from 1 to 4")