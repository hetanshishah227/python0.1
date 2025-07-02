try:
    add=input("Enter your address=> ")
    print(len(add))
    if len(add) < 5:
        raise IndexError("why address is small")

    else:
        print("your addres ",add)
except IndexError as ie:
    print(ie)
except:
    print("error")
