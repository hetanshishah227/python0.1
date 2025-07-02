print("Press 1 for square")
print("Press 2 for cube")
op=int(input("Enter option =>"))

if op==1:
    n=float(input("Enter a number and get its square=>"))
    print("The square is",n*n)
elif op==2:
    n=float(input("Enter a number and get its cube=>"))
    print("The cube is ",n*n*n)
else:
    print("Other")