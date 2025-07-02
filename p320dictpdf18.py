w = {"Mobile Recharge":799,
     "DTH recharge": 999,
     "Clothes":2310,
     "Makeup":3670,
     "Shoes":999
    }

h = {
    "Clothes": 1100,
    "Shoes" :1000,
    "Watch":900,
    "Mobile Recharge":699,
    "Petrol":1980
    }

l1=[]
for k,v in w.items():
    l1.append(v)
print(l1)
print("Total expense of wife is=>",sum(l1))

h1=h.values()
print("Total expense of husband =>",sum(h1))

me=w.values()
mem=max(me)
print(mem)
for k,v in w.items():
    if v==mem:
      print("maximum spent is",mem,"on",k)


he=h.values()
hem=max(he)
print(hem)
for k,v in h.items():
    if v == hem:
        print("maximum spent is",hem,"on",k)
