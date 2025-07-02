n=int(input("Enter limit =>"))
s1=0
c1=0
s2=0
c2=0
for i in range(1,n+1):
    if i%2==0:
        print(i,"is even")
        s1=s1+i
        c1=c1+1
    else:
        s2=s2+i
        c2=c2+1
        print(i,"is odd")
print("sum of even numbers=",s1,"count of even numbers=",c1,"\nsum of odd number=",s2,"count of odd number=",c2)




