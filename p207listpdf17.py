list = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
x = int(input("Enter position=>"))
y = int(input("Enter value=>"))

list[x]=y
print(list)
# or use list.insert(index,value)
list.insert(x,y)
print(list)