import random
c1=0
c2=0
for i in range(1,6):
    x = random.randint(1,50)
    y = random.randint(51,100)

    print("no1=", x, "no2=", y)
    a = int(input("Enter answer of addition=>"))
    if a == x + y:
        print("It's correct")
        print(i,"answer is correct")
        c1=c1+1
    else:
        print("It's incorrect")
        print(i,"answer is incorrect")
        c2 = c2+1


print("total correct answer=>",c1,"\ntotal incorrect answer=>",c2)