students={11:"rahul",33:"manav",45:"mansi",70:"neha",36:"riya",5:"aadesh",7:"kiran",22:"dev",11:"param",17:"aadi",19:"diya"}
print(students)
name = input("Enter a name=>").lower()
for k,v in students.items():
    if name == v:
        print(k)


