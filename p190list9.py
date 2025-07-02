import random

list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
print(list1)
x = int(input("Enter the number of values you want to add=>"))

for i in range(1,x+1):
    y=random.randint(1,50)
    list1.append(y)
print(list1)