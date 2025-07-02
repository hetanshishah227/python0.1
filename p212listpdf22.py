list = ["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]
for x in list:
    if x == "":
        list.remove("")
print(list)