print("Press 1 for PIZZA price")
print("Press 2 for BURGER price")
print("Press 3 for PASTA price")
print("Press 4 for SANDWICH price")
print("Press 5 for JUICE price")

op=int(input("Enter option==> "))

if op==1:
    print("The price of pizza is 500")
    qty=int(input("Enter the quantity of pizza "))
    print(" Your Bill is ",500*qty)

elif op==2:
    print("The price of burger is 400")
    qty=int(input("Enter the quantity of burger "))
    print("Your Bill is ",400*qty)

elif op==3:
    print("The price of pasta is 300")
    qty=int(input("Enter the quantity of pasta "))
    print("Your Bill is ",300*qty)

elif op==4:
    print("The price of sandwich is 200")
    qty=int(input("Enter the quantity of sandwich "))
    print("Your Bill is ",200*qty)

elif op==5:
    print ("The price of juice is 100")
    qty=int(input("Enter the quantity of juice "))
    print("Your Bill is ",100*qty)

else:
    print("Wrong option")

