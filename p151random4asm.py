import random
o = input("Enter one of the operations=> addition, subtraction or multiplication=>").lower()
c1=c2=0
for i in range(1,6):

    if o == "addition":
        x = random.randint(1, 50)
        y = random.randint(51, 100)
        print("no1=", x, "no2=", y)
        a = int(input("Enter the addition of above two numbers=>"))
        if a == x + y:
            print("It's correct")
            c1=c1+1
        else:
            print("It's incorrect")
            print("The correct answer is=>",x+y)
            c2=c2+1

    elif o == "subtraction":
        x = random.randint(1, 50)
        y = random.randint(51, 100)
        print("no1=", x, "no2=", y)
        a = int(input("Enter the subtraction of above two numbers=>"))
        if a == x - y:
            print("It's correct")
            c1=c1+1
        else:
            print("It's incorrect")
            print("The correct answer is=>",x-y)
            c2=c2+1

    elif o == "multiplication":
        x = random.randint(1, 50)
        y = random.randint(51, 100)
        print("no1=", x, "no2=", y)
        a = int(input("Enter the multiplication of above two numbers=>"))
        if a == x + y:
            print("It's correct")
            c1=c1+1
        else:
            print("It's incorrect")
            print("The correct answer is=>",x*y)
            c2=c2+1

    else:
        print("Enter one of the operations=> addition, subtraction or multiplication")

print("Total correct answers are=>",c1,"\nTotal incorrect answers are=>",c2)
