n=int(input("Enter limit =>"))
for i in range(0,n+1):
    if i%2==0:
        print(i,end=" - ")
    else:
        print(i,end=" + ")
