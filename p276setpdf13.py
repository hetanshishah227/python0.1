#The symmetric difference of two sets is the set of elements that are in either of the sets but not in both.
s1 = {11, 22, 33, 44, 55}
s2 = {11, 22, 99, 66, 55}
print(s1.symmetric_difference(s2))
#or
print(s1^s2)