def square():
    a = float(input("Enter a number to get it's square=>"))
    print("The square of the above number is=>",a*a)


def fact():
    a = int(input("Enter a number to get it's factorial=>"))
    f = 1
    for i in range(a, 1, -1):
      f=f*i
    print("Factorial of the above number is=>",f)


def oddeven():
    a = int(input("Enter a number and check whether if it is odd or even=>"))
    if a % 2 == 0:
        print("It is even number")
    else:
        print("It is odd number")


def posneg():
    a = int(input("Enter a number=>"))
    if a > 0:
        print("It is a positive number")
    elif a == 0:
        print("It is zero")
    else:
        print("It is a negative number")


def areaoftri():
    b = float(input("Enter the base of triangle(in cm)=>"))
    h = float(input("Enter the height of triangle(in cm)=>"))
    print("Area of triangle is", 0.5*b*h,"cm")


def areaofcircle():
    r = float(input("Enter the radius of circle(in cm)=>"))
    print("The area of circle is=>",3.14*r*r,"cm")


def table():
    n = int(input("Enter a number and get it's multiplication table=>"))
    for i in range(1,11):
        print(n," X ",i," = ",n*i)


def max3():
    a = int(input("Enter first number=> "))
    b = int(input("Enter second number=> "))
    c = int(input("Enter third number=> "))

    if a > b and a > c:
        print("First number is the greatest number")

    elif b > a and b > c:
        print("Second number is the greatest number")

    elif c > a and c > b:
        print("Third number is the greatest number")

    elif a == b and a > c:
        print("First and Second number are greater numbers")

    elif a == c and a > b:
        print("First and Third are greater numbers")

    elif b == c and b > a:
        print("Second and Third are greater numbers")

    else:
        print("All three numbers are equal")

square()
fact()
oddeven()
posneg()
areaoftri()
areaofcircle()
table()
max3()