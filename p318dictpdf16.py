sp = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
print("press 1 to print the stocks and get the average of its prices in last 3 days")
print("press 2 to add a stock and its price=>")

op = int(input("enter an option. 1 or 2=>"))
if op == 1:
    for k,v in sp.items():
        print(k,"==>",v,"==>","avg:",sum(v)/3)

elif op == 2:
    s = input("Enter stock's name=>").lower()
    p = int(input("Enter stocks price=>"))