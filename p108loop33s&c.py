n=int(input("Enter limit=>"))
s=0
for i in range(1,n+1):
    s=s+i*i
    print(i*i,end=" + ")
print("\nsum=>",s)