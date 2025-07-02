n=int(input("Enter limit=>"))
s=0

for i in range(1,n+1):
    if i%2==0:
        s=s+i*i
        print(i*i,end=" + ")
    else:
        s=s+i*i*i

        print(i*i*i,end=" + ")
print("sum is=>",s)