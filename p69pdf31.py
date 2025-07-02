age=int(input("Enter your age="))
gender=input("Enter your gender (M or F)").lower()
ms=input("Marital status(yes or no)").lower()

if gender=="f" or gender=="m" and 40 < age < 60:
    print("Work only in urban areas")

elif gender=="m" and 20 < age < 40:
    print("You may work anywhere")

else:
    print("ERROR")
