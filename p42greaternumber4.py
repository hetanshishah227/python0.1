n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
n4=int(input("Enter fourth number"))
if n1>n2 and n1>n3 and n1>n4:
    print("First number is greatest number")
elif n2>n1 and n2>n3 and n2>n4:
    print("Second number is greatest number")
elif n3>n1 and n3>n2 and n3>n4:
    print("Third number is greatest number")
elif n4>n1 and n4>n2 and n4>n3:
    print("Fourth number is the greatest number")
else:
    print("All numbers are equal")
                 