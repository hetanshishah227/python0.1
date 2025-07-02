print("What do you want today? A xerox or typing?")
x=input("Enter either xerox or typing=> ").lower()

if x=="xerox":
    print("The cost of a xerox copy is 3 rupees for more than 50 xerox copies and the cost is 5 rupees per copy "
          "for less than 50 copies")
    qty=int(input("Enter the number of xerox copies you want- "))
    if qty>50:
        print("Your Bill is",3*qty)
    elif qty<50:
        print("Your Bill is ",5*qty)

elif x=="typing":
    print("The cost of typing is 50 rupees per page for less than 15 pages and the cost of typing is 20 rupees per page "
          "for more than 15 pages")
    qty=int(input("Enter the number of pages you want typed- "))
    if qty>15:
        print("Your Bill is",qty*20)
    elif qty<15:
        print("Your Bill is",qty*50)

else:
    print("Enter Either xerox or typing")
