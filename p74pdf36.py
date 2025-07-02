age=int(input("Enter your age in years="))

if 0 <= age <= 12:
    print("Child")

elif 13 <= age <= 19:
    print("Teenager")

elif 20 <= age <= 64:
    print("Adult")

else:
    print("Senior citizen")
