n=int(input("enter a numer=> "))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end="")
    print("")