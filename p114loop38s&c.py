n=int(input("Enter limit=>"))
s=0
for i in range(1,n+1):
    print("1/",i,end=" + ")
    s=s+1/i
print("\nsum is",s)