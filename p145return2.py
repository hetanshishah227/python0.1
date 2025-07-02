def areaoftri(b,h):
    a = 0.5*b*h
    print("Area of triangle is =>",a)
    return a

b = int(input("Enter base of triangle=>"))
h = int(input("Enter height of triangle=>"))

c = areaoftri(b,h)
print(c)