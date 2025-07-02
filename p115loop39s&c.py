n=int(input("Enter limit=>"))
f=1
for i in range(n,0,-1):
    print(i,end=" x ")
    f=f*i
print("factorial ",f)

