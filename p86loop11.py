n=int(input("Enter limit=>"))
d=int(input("check divisibility by this number="))
for i in range(1,n+1):
    if i%d==0:
        print(i)
