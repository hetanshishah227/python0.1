def fact():
    n = int(input("Enter a number=>"))
    f = 1
    for i in range(n,1,-1):
        f = f*i
        print("factorial is=>",f)
    return f

c = fact()
print(c)