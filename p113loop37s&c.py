n=int(input("Enter limit=>"))
s=0
for i in range(2,n,2):
    s=s+i
    print(i,end=" + ")
print("sum=> ",s)