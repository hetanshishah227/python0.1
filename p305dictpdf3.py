marks = {
    "ram": 33,
    "rahul": 45,
    "manav": 30,
    "jayul": 34,
    "meena": 29,
    "siddhi": 48
}
n = input("Enter name to search for it in the dictionary=>")
if n in marks:
    print("yes, it exists")
else:
    print("no,it doesn't exists")