while True:

    print("PIZZA price is 500")
    print("BURGER price is 400")
    print("PASTA price is 300")
    print("SANDWICH price is 200")
    print("JUICE price is 100")
    qty1 = int(input("Enter the quantity of pizza=>"))
    print(" Your Pizza Amount is ", 500 * qty1)

    qty2 = int(input("Enter the quantity of burger=>"))
    print("Your Burger Amount is ", 400 * qty2)

    qty3 = int(input("Enter the quantity of pasta=>"))
    print("Your Pasta Amount is ", 300 * qty3)

    qty4 = int(input("Enter the quantity of sandwich=>"))
    print("Your Sandwich Amount is ", 200 * qty4)

    qty5 = int(input("Enter the quantity of juice=>"))
    print("Your Juice Amount is ", 100 * qty5)

    a = 500 * qty1
    b = 400 * qty2
    c = 300 * qty3
    d = 200 * qty4
    e = 100 * qty5

    print("Press 1 for exit and grand total")
    n=int(input("Enter 1=>"))
    if n==1:
        print("Your grand total is=>",a+b+c+d+e)
    else:
        print("Press 1")


