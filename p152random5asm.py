import random
c1=c2=0
for i in range(1,6):

    op = random.randint(1,3)
    print(op)

    if op == 1:
        x = random.randint(1, 50)
        y = random.randint(51, 100)
        print("no1=", x, "no2=", y)
        a = int(input("Enter the addition of above 2 numbers=>"))
        if a == x + y:
            print("It's correct")
            c1 = c1 + 1
        else:
            print("It's incorrect")
            print("The correct answer is=>", x + y)
            c2 = c2 + 1

    elif op == 2:
        x = random.randint(1, 50)
        y = random.randint(51, 100)
        print("no1=", x, "no2=", y)
        a = int(input("Enter the subtraction of above 2 numbers=>"))
        if a == x - y:
            print("It's correct")
            c1 = c1 + 1
        else:
            print("It's incorrect")
            print("The correct answer is=>", x - y)
            c2 = c2 + 1

    else:
        x = random.randint(1, 50)
        y = random.randint(51, 100)
        print("no1=", x, "no2=", y)
        a = int(input("Enter the multiplication of above 2 numbers=>"))
        if a == x * y:
            print("It's correct")
            c1 = c1 + 1
        else:
            print("It's incorrect")
            print("The correct answer is=>", x * y)
            c2 = c2 + 1

    print("Total correct answers are=>",c1,"\nTotal incorrect answers are=>",c2)


