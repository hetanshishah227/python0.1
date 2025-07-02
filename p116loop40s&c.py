n=int(input("Enter limit=>"))
s=0
for i in range(5,n,5):
    s=s+i
    print(i,end=" + ")
print("sum is",s)