n=int(input("Enter limit =>"))
s=0
c=0
for i in range(1,n+1):
    if i%7==0:
        print(i)
        s=s+i
        c=c+1

print("sum = ",s," count = ",c)