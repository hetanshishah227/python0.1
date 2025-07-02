try:
    eng=int(input("enter your english marks=> "))
    hindi=int(input("enter your hindi marks=> "))
    if eng < 0:
     raise IndexError("why you enter less than 0 in english")
    elif hindi < 0:
        raise IndexError("why u entered less than 0 in hindi")
    else:
        print("Your total marks are=> ",eng+hindi)
except IndexError as ie:
    print(ie)
except:
    print("error")
