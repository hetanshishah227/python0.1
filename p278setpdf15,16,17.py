#15
#Use the difference() method or - operator to get elements that are in one set but not the other.
s1 = {11, 22, 33, 44, 55}
s2 = {33, 44}
print(s1.difference(s2))
print(s1-s2)

#16
#Use the union() method or | operator to combine all elements from multiple sets.
s1 = {11, 22}
s2 = {33, 44}
s3 = {55, 66}

print( s1|s2|s3)
print(s1.union(s2,s3))

#17
#Use the clear() method to empty the set.
s1 = {11,22,33}
s1.clear()
print(s1)

