#f1=open("abc","r")
#list1=list(f1)
#print(list1)
#list1.reverse()
#print(list1)

f1=open("abc","r")

list1 = list(f1)
list1.reverse()
for x in list1:
    print(x,end="")
f1.close()