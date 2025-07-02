# 5
tupleD=(11,22,28,42,56,11,99,33,70,35)
s = 0
c = 0
for x in tupleD:
    if x % 7 == 0:
        print(x)
        s = s + x
        c = c + 1
print("count is",c)
print("sum =",s)