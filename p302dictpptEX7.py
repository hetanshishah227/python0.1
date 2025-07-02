students={11:"rahul",33:"manav",45:"mansi",70:"neha",36:"riya",5:"aadesh",7:"kiran",22:"dev",11:"param",17:"aadi",19:"diya"}

print("Press 1 to view passed students")
print("Press 2 to view failed students")
print("Press 3 to view both passed and failed students")
choice = int(input("Enter your choice=>"))
if choice == 1:
    for k in students:
        if k > 33:
            print(students[k])
elif choice == 2:
    for k in students:
        if k >= 33:
            print(students[k])
elif choice == 3:
    for k in students:
        print(students[k])
else:
    print("Enter 1,2 or 3")