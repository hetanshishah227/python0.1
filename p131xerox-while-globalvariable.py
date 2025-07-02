a=b=c=d=0
while True:
    print("Press 1 for Xerox")
    print("Press 2 for Typing")
    print("Press 3 for Exit and Grand total")
    n=int(input("Enter 1,2 or 3=>"))

    if n==1:
        print("The cost of a xerox is 3 rupees for more than 50 xerox copies and the cost is 5 rupees per copy for less"
              "than 50 copies")
        qty1 = int(input("Enter the number of xerox copies you want- "))
        if qty1 > 50:
            a=3*qty1
            print("Your Xerox Amount is", a)
        elif qty1 < 50:
            b=5*qty1
            print("Your Xerox Amount is", b)


    elif n == 2:
        print("The cost of typing is 50 rupees per page for less than 15 pages and the cost of typing is 20 rupees per page "
            "for more than 15 pages")
        qty2 = int(input("Enter the number of pages you want typed- "))
        if qty2 > 15:
            c=20*qty2
            print("Your Typing Amount is", c)
        elif qty2 < 15:
            d=50*qty2
            print("Your Typing Amount is", d)


    elif n==3:
        print("Your grand total is=>",a+b+c+d)
        break

    else:
        print("Enter 1,2 or 3=>")
