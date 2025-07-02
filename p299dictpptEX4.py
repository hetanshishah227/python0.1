students={11:"rahul",33:"manav",45:"mansi",70:"neha",36:"riya",5:"aadesh",7:"kiran",22:"dev",11:"param",17:"aadi",19:"diya"}
c1 = 0
c2 = 0
for k in students:
      if k > 33:
          c1 = c1 + 1
          print(students[k],"pass",c1)
      else:
          c2 = c2 + 1
          print(students[k],"fail",c2)

print("Total number of students passed are=>",c1)
print("Total number of students failed are=>",c2)