me = {"January":2200,
      "February":2350,
      "March":2600,
      "April":2130,
      "May":2190,
      "June":1980,
      "July":2400,
      "August":2250,
      "September":2100,
      "October":2400,
      "November":2150,
      "December":2500
      }
#1
feb1=me["February"]
jan1=me["January"]

print("extra dollars spent in february=>",feb1-jan1)

#2
mar1=me["March"]
print("total expense for the first quarter=>",jan1+feb1+mar1)

#3
for k,v in me.items():
    if v == 2400:
        print(k,"exact expense is 2400 dollars")

#4
e = int(input("enter your expense for june in dollars=>"))
me["June"]=e
print(me)

#5
me["April"]=2130+200
print(me)

#6
m=me.values()
print(m)
m1=max(m)
#print(sum(m))
print(max(m))

for k,v in me.items():
      if v==m1:
            print(k,v)

#7
feb1=me["February"]
jan1=me["January"]
mar1=me["March"]
apr1=me["April"]
may1=me["May"]
jun1=me["June"]
print("average monthly expense for the first half of the year=>",(jan1+feb1+mar1+apr1+may1+jun1)/6,"dollars")

#or
me1 = me.values()
print(me1)
c = 0
s = 0
for x in me1:
    if c==5:
          break
    s=s+x
    c=c+1

print("Sum = ",s," Avg = ",s/5)

#8
m=me.values()
ml=min(m)
for k,v in me.items():
      if v == ml:
            print("lowest expense is",ml,"in the month",k)
