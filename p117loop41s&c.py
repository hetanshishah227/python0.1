n=int(input("Enter limit=>"))
s=0
for i in range(9,n,10):
    print(i,end=" + ")
    s=s+i
print("sum is=>",s)