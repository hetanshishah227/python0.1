# 4
c = 0
s = 0
tupleD=(11,22,33,44,55,11,99,33)
for x in tupleD:
    if x % 2 == 0:
        print(x)
        c = c + 1
        s = s + x
print("sum =",s)
print("count is",c)