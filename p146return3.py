def max3(a,b,c):

    if a > b and a > c:
        print("First number is the greatest number")
        return a

    elif b > a and b > c:
        print("Second number is the greatest number")
        return b

    elif c > a and c > b:
        print("Third number is the greatest number")
        return c

    elif a == b and a > c:
        print("First and Second number are greater numbers")
        return a,b

    elif a == c and a > b:
        print("First and Third are greater numbers")
        return a,c

    elif b == c and b > a:
        print("Second and Third are greater numbers")
        return b,c
    else:
        print("All three numbers are equal")
        return a,b,c

a = int(input("Enter first number=> "))
b = int(input("Enter second number=> "))
c = int(input("Enter third number=> "))


d = max3(a,b,c)
print(d)
