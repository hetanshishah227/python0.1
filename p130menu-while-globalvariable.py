a=b=c=d=e=0
while True:
        print("Press 1 for PIZZA price")
        print("Press 2 for BURGER price")
        print("Press 3 for PASTA price")
        print("Press 4 for SANDWICH price")
        print("Press 5 for JUICE price")
        print("Press 6 for exit and grand total=>")

        op=int(input("Enter option==> "))

        if op==1:
            print("The price of pizza is 500")
            qty1=int(input("Enter the quantity of pizza "))
            a = 500 * qty1
            print(" Your Bill is ",a)

        elif op==2:
            print("The price of burger is 400")
            qty2=int(input("Enter the quantity of burger "))
            b=400*qty2
            print("Your Bill is ",b)

        elif op==3:
            print("The price of pasta is 300")
            qty3=int(input("Enter the quantity of pasta "))
            c=300*qty3

            print("Your Bill is ",c)

        elif op==4:
            print("The price of sandwich is 200")
            qty4=int(input("Enter the quantity of sandwich "))
            d=200*qty4
            print("Your Bill is ",d)

        elif op==5:
            print ("The price of juice is 100")
            qty5=int(input("Enter the quantity of juice "))
            e=100*qty5
            print("Your Bill is ",e)

        elif op==6:
            print("The grand total is",a+b+c+d+e)
            break

        else:
            print("Wrong option")
