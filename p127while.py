while True:
    print("Press 1 for Square")
    print("Press 2 for Cube")
    print("Press 3 for exit")
    n=int(input("Enter 1 or 2 or 3=>"))
    if n==1:
        z = int(input("Enter a number=>"))
        print("Square of number is=",z*z)

    elif n==2:
        z = int(input("Enter a number=>"))
        print("Cube of number is=",z*z*z)
    elif n==3:
        print("Bye")
        break
    else:
        print("Enter 1 or 2 or 3")

