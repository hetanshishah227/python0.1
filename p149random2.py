import random
x = random.randint(1,50)
y = random.randint(51,100)
print("no1=",x,"no2=",y)
a = int(input("Enter answer of addition=>"))
if a == x+y:
    print("It's correct")
else:
    print("It's incorrect")