def max2(a,b):
    if a > b:
        return a
    elif a == b:
        return a,b
    else:
        return b

a = int(input("Enter a number=>"))
b = int(input("Enter another number=>"))

c = max2(a,b)
print(c)