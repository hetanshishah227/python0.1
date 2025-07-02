n1=float(input("Enter first number"))
n2=float(input("Enter second number"))
n3=float(input("Enter third number"))
if n1>n2 and n1>n3:
    print("First number is greatest number")
elif n2>n1 and n2>n3:
    print("Second number is greatest number")
elif n3>n2 and n3>n1:
    print("Third number is greatest number")
elif n1==n2 and n1 > n3:
    print("First and Second number are greater numbers")
elif n1==n3 and n1 > n2:
    print("First and Third are greater numbers")
elif n2==n3 and n2 > n1:
    print("Second and Third are greater numbers")
else:
    print("All are equal")

