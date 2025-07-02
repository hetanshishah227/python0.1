list = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
list2=[]
for x in list:
    if x % 2 != 0:
        list2.append(x)


list=list2
print(list2)