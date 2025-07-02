list1 = [11, 44, 500]
list2 = [77, 44, 11]
list3 = []
for x in list1:
    if x in list2:
        list3.append(x)
print(list3)