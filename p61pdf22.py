yr=int(input("Enter any year "))
month=int(input("Enter any month number "))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("It has 31 days")
elif yr%4==0 and month==2:
    print("It has 29 days")
else:
    print("It has 28 days")
