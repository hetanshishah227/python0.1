z=int(input("Enter an integer-"))

if z<0:
    print("Enter an integer")
else:
    if z%2!=0:
        print("weird")
    elif z%2==0:
        if 2 <= z <= 5:
            print("Not weird")
        elif 6 <= z <= 20:
            print("Weird")
        elif z > 20:
            print("Not weird")
