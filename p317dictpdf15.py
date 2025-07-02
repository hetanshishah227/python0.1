cp = {"china":143,"india":143,"usa":32,"uk":21}
print("press 1 for print")
print("press 2 to add a country name with it's population in the list")
print("press 3 to remove a country from the dictionary")
print("press 4 to know the country's population")
op = int(input("enter a number from 1 to 4=>"))

if op == 1:
    for k,v in cp.items():
        print(k,"==>",v)

elif op == 2:
    cn = input("enter a country name to add=>").lower()
    if cn in cp:
        print("it already exists in the dictionary")
    else:
        p = int(input("enter the population of the country entered (in crores)=>"))
        cp[cn]=p
        print(cp)

elif op == 3:
    cr = input("enter the country's name to remove it=>").lower()
    if cr in cp:
        del cp[cr]
        print(cp)

elif op == 4:
    cq = input("enter the country's name to know its population=>").lower()
    if cq in cp:
        print("the population is",cp[cq],"crores")
    else:
        print("this country doesnt exists in the dictionary")

else:
    print("enter a number from 1 to 4")