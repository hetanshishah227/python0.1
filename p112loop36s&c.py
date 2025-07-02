n=int(input("Enter limit=>"))
s=0
for i in range(1,n,2):
    s=s+i
    print(i,end=" + ")
print("\nsum is=>",s)