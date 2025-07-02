d1 = {1: "Alice", 2: "Bob",3: "Charlie",4: "David",5: "Eve",6: "Frank",7: "Grace",8: "Hannah",9: "Ian",10: "Jack"}
print(d1)
for k,v in d1.items():
    if len(v)>4:
        print(k,v)
